const API_URL = "/products";

let products = [];

const $ = id => document.getElementById(id);

const inventoryBody = $("inventory-body");
const editorModal = $("editor-modal");
const productForm = $("product-form");
const adminSearch = $("admin-search");
const adminMessage = $("admin-message");
const formError = $("form-error");


// Product fields

const textFields = [
    "item_name",
    "description",
    "category",
    "scale",
    "material",
    "image_url"
];

const numberFields = [
    "height_cm",
    "width_cm",
    "depth_cm",
    "price",
    "quantity",
    "production_days"
];

const booleanFields = [
    "painted",
    "made_to_order",
    "is_active"
];


// Escape HTML

function escapeHTML(value) {
    return String(value ?? "").replace(/[&<>"']/g, char => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[char]);
}


// Format prices

function formatPrice(price) {
    return new Intl.NumberFormat("hu-HU", {
        style: "currency",
        currency: "HUF",
        maximumFractionDigits: 0
    }).format(price);
}


// API request helper

async function apiRequest(url, options = {}) {

    const response = await fetch(url, {
        headers: {
            "Content-Type": "application/json"
        },
        ...options
    });

    if (!response.ok) {

        const error = await response.json().catch(() => ({}));

        let message = `HTTP error: ${response.status}`;

        if (typeof error.detail === "string") {
            message = error.detail;
        }

        if (Array.isArray(error.detail)) {
            message = error.detail.map(item =>
                `${item.loc.join(".")}: ${item.msg}`
            ).join("\n");
        }

        throw new Error(message);
    }

    if (response.status === 204) {
        return null;
    }

    return response.json();
}


// Load products

async function loadProducts() {

    try {

        products = await apiRequest(API_URL);

        updateStatistics();
        renderInventory();

    } catch (error) {

        adminMessage.textContent = error.message;

        inventoryBody.innerHTML = `
            <tr>
                <td colspan="7">
                    Unable to load products.
                </td>
            </tr>
        `;
    }
}


// Dashboard statistics

function updateStatistics() {

    const totalProducts = products.length;

    const activeProducts = products.filter(
        product => product.is_active
    ).length;

    const totalStock = products.reduce(
        (total, product) => total + product.quantity,
        0
    );

    const inventoryValue = products.reduce(
        (total, product) =>
            total + product.price * product.quantity,
        0
    );

    $("stat-total").textContent = totalProducts;
    $("stat-active").textContent = activeProducts;
    $("stat-stock").textContent = totalStock;
    $("stat-value").textContent = formatPrice(inventoryValue);
}


// Product thumbnail

function productThumbnail(product) {

    const placeholder = `
        <div class="table-placeholder">HC</div>
    `;

    if (!product.image_url) {
        return placeholder;
    }

    try {

        const url = new URL(
            product.image_url,
            window.location.origin
        );

        if (!["http:", "https:"].includes(url.protocol)) {
            return placeholder;
        }

        return `
            <img
                class="table-thumbnail"
                src="${escapeHTML(url.href)}"
                alt="${escapeHTML(product.item_name)}"
            >
        `;

    } catch {
        return placeholder;
    }
}


// Render inventory table

function renderInventory() {

    const search = adminSearch.value.toLowerCase().trim();

    const filteredProducts = products.filter(product => {

        const searchableText = `
            ${product.id}
            ${product.item_name}
            ${product.category || ""}
            ${product.description || ""}
        `.toLowerCase();

        return searchableText.includes(search);
    });

    if (filteredProducts.length === 0) {

        inventoryBody.innerHTML = `
            <tr>
                <td colspan="7">
                    No products found.
                </td>
            </tr>
        `;

        return;
    }

    inventoryBody.innerHTML = filteredProducts.map(product => `

        <tr>

            <td>#${product.id}</td>

            <td>
                <div class="table-product">

                    ${productThumbnail(product)}

                    <span>
                        ${escapeHTML(product.item_name)}
                    </span>

                </div>
            </td>

            <td>
                ${escapeHTML(product.category || "—")}
            </td>

            <td>
                ${formatPrice(product.price)}
            </td>

            <td>
                ${product.quantity}
            </td>

            <td>
                <span class="${
                    product.is_active
                        ? "status-active"
                        : "status-inactive"
                }">
                    ${product.is_active ? "Active" : "Hidden"}
                </span>
            </td>

            <td>

                <button
                    class="action-button"
                    data-action="edit"
                    data-id="${product.id}"
                >
                    Edit
                </button>

                <button
                    class="action-button"
                    data-action="toggle"
                    data-id="${product.id}"
                >
                    ${product.is_active ? "Hide" : "Publish"}
                </button>

                <button
                    class="action-button delete-button"
                    data-action="delete"
                    data-id="${product.id}"
                >
                    Delete
                </button>

            </td>

        </tr>

    `).join("");
}


// Open new product editor

function openNewProduct() {

    productForm.reset();

    $("product-id").value = "";
    $("editor-title").textContent = "Add product";

    formError.textContent = "";

    editorModal.showModal();
}


// Open existing product editor

async function editProduct(productId) {

    try {

        const product = await apiRequest(
            `${API_URL}/${productId}`
        );

        productForm.reset();

        $("product-id").value = product.id;

        $("editor-title").textContent = "Edit product";

        textFields.forEach(field => {
            $(field).value = product[field] ?? "";
        });

        numberFields.forEach(field => {
            $(field).value = product[field] ?? "";
        });

        booleanFields.forEach(field => {
            $(field).checked = Boolean(product[field]);
        });

        formError.textContent = "";

        editorModal.showModal();

    } catch (error) {
        adminMessage.textContent = error.message;
    }
}


// Collect form data

function collectFormData() {

    const data = {};

    textFields.forEach(field => {

        const value = $(field).value.trim();

        data[field] = value || null;
    });

    numberFields.forEach(field => {

        const value = $(field).value;

        data[field] = value === ""
            ? null
            : Number(value);
    });

    booleanFields.forEach(field => {
        data[field] = $(field).checked;
    });

    return data;
}


// Create or update product

async function saveProduct(event) {

    event.preventDefault();

    formError.textContent = "";

    const productId = $("product-id").value;
    const productData = collectFormData();

    const isEditing = Boolean(productId);

    const url = isEditing
        ? `${API_URL}/${productId}`
        : API_URL;

    const method = isEditing
        ? "PUT"
        : "POST";

    const submitButton = productForm.querySelector(
        'button[type="submit"]'
    );

    submitButton.disabled = true;

    try {

        await apiRequest(url, {
            method: method,
            body: JSON.stringify(productData)
        });

        editorModal.close();

        adminMessage.textContent = isEditing
            ? "Product updated successfully."
            : "Product created successfully.";

        await loadProducts();

    } catch (error) {

        formError.textContent = error.message;

    } finally {

        submitButton.disabled = false;
    }
}


// Hide or publish product

async function toggleProduct(productId) {

    try {

        const product = await apiRequest(
            `${API_URL}/${productId}`
        );

        const { id, ...productData } = product;

        productData.is_active = !product.is_active;

        await apiRequest(`${API_URL}/${productId}`, {
            method: "PUT",
            body: JSON.stringify(productData)
        });

        adminMessage.textContent = productData.is_active
            ? "Product published successfully."
            : "Product hidden successfully.";

        await loadProducts();

    } catch (error) {
        adminMessage.textContent = error.message;
    }
}


// Delete product

async function deleteProduct(productId) {

    const product = products.find(
        product => product.id === Number(productId)
    );

    const confirmed = confirm(
        `Delete "${product?.item_name || "this product"}"?\n\n` +
        "This action cannot be undone."
    );

    if (!confirmed) {
        return;
    }

    try {

        await apiRequest(`${API_URL}/${productId}`, {
            method: "DELETE"
        });

        adminMessage.textContent =
            "Product deleted successfully.";

        await loadProducts();

    } catch (error) {
        adminMessage.textContent = error.message;
    }
}


// Event listeners

$("add-product").addEventListener(
    "click",
    openNewProduct
);

$("close-editor").addEventListener("click", () => {
    editorModal.close();
});

$("cancel-editor").addEventListener("click", () => {
    editorModal.close();
});

productForm.addEventListener("submit", saveProduct);

adminSearch.addEventListener("input", renderInventory);


inventoryBody.addEventListener("click", event => {

    const button = event.target.closest("[data-action]");

    if (!button) {
        return;
    }

    const productId = button.dataset.id;
    const action = button.dataset.action;

    if (action === "edit") {
        editProduct(productId);
    }

    if (action === "toggle") {
        toggleProduct(productId);
    }

    if (action === "delete") {
        deleteProduct(productId);
    }
});


// Initialize dashboard

loadProducts();