from typing import Any
import streamlit as st
import requests


def api_request(
    method: str,
    api_url: str,
    endpoint: str,
    item_data: dict | None = None
) -> tuple[bool, Any]:

    try:
        response = requests.request(
            method=method,
            url=f"{api_url.rstrip('/')}{endpoint}",
            json=item_data,
            timeout=5
        )

        response.raise_for_status()

        if response.status_code == 204 or not response.content:
            return True, None

        return True, response.json()

    except requests.exceptions.ConnectionError:
        st.error("Nem sikerült kapcsolódni a FastAPI szerverhez.")

    except requests.exceptions.Timeout:
        st.error("A FastAPI szerver nem válaszolt időben.")

    except requests.exceptions.HTTPError as exc:
        st.error(f"API hiba: {exc}")

    except requests.exceptions.RequestException as exc:
        st.error(f"Kommunikációs hiba: {exc}")

    return False, None

# --------------- select (GET) -----------------
def get_items(api_url: str) -> list[dict] | None:
    success, data = api_request("GET", api_url, "/items/")
    return data if success else None

# --------------- create (POST) -------------
def create_item(api_url: str, item_data: dict) -> dict | None:
    success, data = api_request(
        "POST", api_url, "/items/", item_data
    )
    return data if success else None

# -------------- update (PUT) ------------------
def update_item(api_url: str, item_id: str, item_data: dict) -> dict | None:
    success, data = api_request(
        "PUT", api_url, f"/items/{item_id}", item_data
    )
    return data if success else None

# -------------- delete (DELETE) -----------------
def delete_item(api_url: str, item_id: str) -> bool:
    success, _ = api_request(
        "DELETE", api_url, f"/items/{item_id}"
    )
    return success
