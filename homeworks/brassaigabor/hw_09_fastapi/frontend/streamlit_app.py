import streamlit as st
import pandas as pd
#import requests
from frontend import streamlit_data_moving as api

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="hw_09_fastapi webshop",
    page_icon="🛒",
    layout="wide"
)

st.title("Webshop termékkezelő")
#st.header("Terméknyilvántartó alkalmazás - FastAPI")
st.caption("Terméknyilvántartó alkalmazás - FastAPI")

if "editor_version" not in st.session_state:
    st.session_state["editor_version"] = 0

# Korábbi mentés eredményének megjelenítése
save_result = st.session_state.pop("save_result", None)

if save_result is not None:
    saved = save_result["saved"]
    errors = save_result["errors"]

    message = (
        f"Új: {saved['created']} | "
        f"Módosított: {saved['updated']} | "
        f"Törölt: {saved['deleted']}"
    )

    if errors:
        st.warning(f"Részleges mentés: {message}")
        for error in errors:
            st.error(error)
    else:
        st.success(f"Sikeres mentés! {message}")

# --------------------------------------------------------
def prepare_item_data(row: dict) -> dict:
    item_name = row.get("item_name")
    quantity = row.get("quantity")
    price = row.get("price")
    category = row.get("category")

    if pd.isna(item_name) or not str(item_name).strip():
        raise ValueError("A termék neve kötelező!")

    if pd.isna(quantity) or pd.isna(price):
        raise ValueError("A mennyiség és az ár kötelező!")

    return {
        "item_name": str(item_name).strip(),
        "quantity": int(quantity),
        "price": int(price),
        "category": (
            None
            if pd.isna(category) or not str(category).strip()
            else str(category).strip()
        )
    }

# ----------------------------------------------
def save_changes(original_df: pd.DataFrame, editor_state: dict):

    saved = {
        "created": 0,
        "updated": 0,
        "deleted": 0
    }

    errors = []

    deleted_indices = {
        int(index) for index in editor_state["deleted_rows"]
    }

    # 1. DELETE – törölt termékek
    for index in sorted(deleted_indices):

        item_id = str(original_df.iloc[index]["id"])

        if api.delete_item(API_URL, item_id):
            saved["deleted"] += 1
        else:
            errors.append(f"Törlés sikertelen: {item_id}")

    # 2. PUT – módosított termékek
    for index, changes in editor_state["edited_rows"].items():

        index = int(index)

        # A törölt terméket nem módosítjuk
        if index in deleted_indices:
            continue

        original_item = original_df.iloc[index].to_dict()

        # Az eredeti adatokra rávezetjük a módosításokat
        original_item.update(changes)

        item_id = str(original_item["id"])

        try:
            item_data = prepare_item_data(original_item)
        except (ValueError, TypeError, OverflowError) as exc:
            errors.append(f"Módosítás ({item_id}): {exc}")
            continue

        if api.update_item(API_URL, item_id, item_data) is not None:
            saved["updated"] += 1
        else:
            errors.append(f"Módosítás sikertelen: {item_id}")

    # 3. POST – új termékek
    for new_item in editor_state["added_rows"]:

        try:
            item_data = prepare_item_data(new_item)
        except (ValueError, TypeError, OverflowError) as exc:
            errors.append(f"Új termék: {exc}")
            continue

        if api.create_item(API_URL, item_data) is not None:
            saved["created"] += 1
        else:
            errors.append("Új termék létrehozása sikertelen.")

    return saved, errors
#------------------------------------------------

st.subheader("Terméklista")

items = api.get_items(API_URL)

if items is None:
    st.warning("A terméklista nem tölthető be.")

else:
    if not items:
        st.info("Még nincs termék az adatbázisban.")

    # data_frame létrehozása
    items_df = pd.DataFrame(
        items,
        columns=[
            "id",
            "item_name",
            "quantity",
            "price",
            "category"
        ]
    )

    # st.data_editor
    editor_key = f"items_editor_{st.session_state['editor_version']}"

    # st.data_editor paraméterezése
    st.data_editor(
        items_df,
        width="stretch",
        hide_index=True,
        num_rows="dynamic",
        disabled=["id"],
        key=editor_key,
        column_config={
            "id": "Azonosító",
            "item_name": st.column_config.TextColumn(
                "Termék neve",
                required=True
            ),
            "quantity": st.column_config.NumberColumn(
                "Mennyiség",
                min_value=0,
                step=1
            ),
            "price": st.column_config.NumberColumn(
                "Ár (Ft)",
                min_value=0,
                step=1,
                format="%d Ft"
            ),
            "category": st.column_config.TextColumn(
                "Kategória"
            )
        }
    )

    editor_state = st.session_state[editor_key]

    # a gomb állaoota enable/desable attól függően, volt-e változas
    has_changes = bool(
        editor_state["edited_rows"]
        or editor_state["added_rows"]
        or editor_state["deleted_rows"]
    )

    if st.button(
        "Módosítások mentése",
        type="primary",
        disabled=not has_changes        # gomb allapota attol fugg, volt-e valtozas a tablazatban
    ):
        saved, errors = save_changes(items_df, editor_state)

        st.session_state["save_result"] = {
            "saved": saved,
            "errors": errors
        }

        # A régi táblázatállapot eldobása
        st.session_state["editor_version"] += 1

        # Új adatok lekérése az adatbázisból
        st.rerun()

    # st.subheader("Változtatások")

    # st.write("Módosított cellák:")
    # st.write(editor_state["edited_rows"])

    # st.write("Új sorok:")
    # st.write(editor_state["added_rows"])

    # st.write("Törölt sorok:")
    # st.write(editor_state["deleted_rows"])
