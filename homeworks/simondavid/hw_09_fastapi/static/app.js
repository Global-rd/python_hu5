const API_URL = "/products";

let products = [];

const productGrid = document.getElementById("product-grid");
const searchInput = document.getElementById("search-input");
const categoryFilter = document.getElementById("category-filter");
const sortFilter = document.getElementById("sort-filter");
const productCount = document.getElementById("product-count");

const productModal = document.getElementById("product-modal");
const modalContent = document.getElementById("modal-content");
const closeModal = document.getElementById("close-modal");


// Escape HTML to prevent injected markup

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


// Product image

function productImage(product) {
    const placeholder = `
        <div class="image-placeholder">HC</div>
    `;

    if (!product.image_url) {
        return placeholder;
    }

    try {
        const url = new URL(product.image_url, window.location.origin);

        if (!["http:", "https:"].includes(url.protocol)) {
            return placeholder;
        }

        return `
            <img
                class="product-image"
                src="${escapeHTML(url.href)}"
                alt="${escapeHTML(product.item_name)}"
                loading="lazy"
            >
        `;
    } catch {
        return placeholder;
    }
}


// Product availability

function getAvailability(product) {

    if (product.quantity > 0) {
        return `In stock — ${product.quantity} available`;
    }

    if (product.made_to_order) {
        return `Made to order — ${product.production_days} days`;
    }

    return "Currently unavailable";
}


// Load products from FastAPI

async function loadProducts() {

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();

        products = data.filter(product => product.is_active);

        loadCategories();
        renderProducts();

    } catch (error) {

        console.error("Failed to load products:", error);

        productGrid.innerHTML = `
            <p class="empty-state">
                Unable to load collectibles.
                Please try again later.
            </p>
        `;
    }
}


// Populate category filter

function loadCategories() {

    const categories = [...new Set(
        products
            .map(product => product.category)
            .filter(Boolean)
    )].sort();

    categoryFilter.innerHTML = `
        <option value="">All categories</option>
    `;

    categories.forEach(category => {

        const option = document.createElement("option");

        option.value = category;
        option.textContent = category;

        categoryFilter.appendChild(option);
    });
}


// Search, filter and sort products

function getFilteredProducts() {

    const search = searchInput.value.toLowerCase().trim();
    const category = categoryFilter.value;
    const sort = sortFilter.value;

    let filtered = products.filter(product => {

        const searchableText = `
            ${product.item_name}
            ${product.description || ""}
            ${product.category || ""}
        `.toLowerCase();

        const matchesSearch = searchableText.includes(search);

        const matchesCategory =
            !category || product.category === category;

        return matchesSearch && matchesCategory;
    });

    if (sort === "price-asc") {
        filtered.sort((a, b) => a.price - b.price);
    }

    if (sort === "price-desc") {
        filtered.sort((a, b) => b.price - a.price);
    }

    if (sort === "name") {
        filtered.sort((a, b) =>
            a.item_name.localeCompare(b.item_name)
        );
    }

    return filtered;
}


// Render product cards

function renderProducts() {

    const filteredProducts = getFilteredProducts();

    productCount.textContent =
        `${filteredProducts.length} collectible(s) found`;

    if (filteredProducts.length === 0) {

        productGrid.innerHTML = `
            <p class="empty-state">
                No collectibles found.
            </p>
        `;

        return;
    }

    productGrid.innerHTML = filteredProducts.map(product => `

        <article class="product-card">

            ${productImage(product)}

            <div class="product-info">

                <p class="product-category">
                    ${escapeHTML(product.category || "Collectibles")}
                </p>

                <h3 class="product-name">
                    ${escapeHTML(product.item_name)}
                </h3>

                <p class="product-description">
                    ${escapeHTML(product.description || "")}
                </p>

                <div class="product-specs">

                    ${product.scale ? `
                        <span class="spec-tag">
                            ${escapeHTML(product.scale)}
                        </span>
                    ` : ""}

                    ${product.height_cm ? `
                        <span class="spec-tag">
                            ${product.height_cm} cm
                        </span>
                    ` : ""}

                    <span class="spec-tag">
                        ${escapeHTML(product.material)}
                    </span>

                    <span class="spec-tag">
                        ${product.painted ? "Painted" : "Unpainted"}
                    </span>

                </div>

                <p class="product-price">
                    ${formatPrice(product.price)}
                </p>

                <p class="availability">
                    ${getAvailability(product)}
                </p>

                <button
                    class="outline-button"
                    data-product-id="${product.id}"
                >
                    View details
                </button>

            </div>

        </article>

    `).join("");
}


// Product details

async function showProductDetails(productId) {

    try {
        const response = await fetch(`${API_URL}/${productId}`);

        if (!response.ok) {
            throw new Error("Product not found");
        }

        const product = await response.json();

        if (!product.is_active) {
            throw new Error("Product unavailable");
        }

        modalContent.innerHTML = `

            <div class="modal-layout">

                <div>
                    ${productImage(product)}
                </div>

                <div>

                    <p class="product-category">
                        ${escapeHTML(product.category || "Collectibles")}
                    </p>

                    <h2>
                        ${escapeHTML(product.item_name)}
                    </h2>

                    <p class="product-price">
                        ${formatPrice(product.price)}
                    </p>

                    <p>
                        ${escapeHTML(product.description || "")}
                    </p>

                    <hr style="
                        border: 0;
                        border-top: 1px solid #302a23;
                        margin: 20px 0;
                    ">

                    <p><strong>Scale:</strong>
                        ${escapeHTML(product.scale || "Not specified")}
                    </p>

                    <p><strong>Height:</strong>
                        ${product.height_cm ? product.height_cm + " cm" : "N/A"}
                    </p>

                    <p><strong>Width:</strong>
                        ${product.width_cm ? product.width_cm + " cm" : "N/A"}
                    </p>

                    <p><strong>Depth:</strong>
                        ${product.depth_cm ? product.depth_cm + " cm" : "N/A"}
                    </p>

                    <p><strong>Material:</strong>
                        ${escapeHTML(product.material)}
                    </p>

                    <p><strong>Finish:</strong>
                        ${product.painted ? "Painted" : "Unpainted"}
                    </p>

                    <p><strong>Production time:</strong>
                        ${product.production_days} days
                    </p>

                    <p class="availability">
                        ${getAvailability(product)}
                    </p>

                </div>

            </div>
        `;

        productModal.showModal();

    } catch (error) {

        console.error(error);
        alert("Unable to load product details.");
    }
}


// Event listeners

searchInput.addEventListener("input", renderProducts);

categoryFilter.addEventListener("change", renderProducts);

sortFilter.addEventListener("change", renderProducts);


productGrid.addEventListener("click", event => {

    const button = event.target.closest("[data-product-id]");

    if (button) {
        showProductDetails(button.dataset.productId);
    }
});


closeModal.addEventListener("click", () => {
    productModal.close();
});


productModal.addEventListener("click", event => {

    if (event.target === productModal) {
        productModal.close();
    }
});


// Initialize storefront

loadProducts();