# a routerek határozzák meg az endpointokat
# küldök egy requestet az endpointra
# az meghívja a servicet
# a service meghívja az adatbázis műveletet

# Itt adjuk meg, hogy melyik endpointra milyen requestet várunk

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import Product
from schemas import ProductRequest, ProductResponse
from services.products import (
    list_products_service,
    insert_product_service,
    get_product_service,
    update_product_service,
    delete_product_service
)



# Nem akarom begépelni minden endpointhoz begépelni hogy mind a productra jöjjön. Egyszer létrehozom hogy /product
router = APIRouter(
    prefix="/products",
    tags=["products"]
)

# szeretnék egy endpointot írni, ami get requestet fogad 
# egy endpointnál elég megadni egy / jelet, mert mindent a productnál fog kezdeni. 
# Ha több endpont lenne, akkor a routernél kell létre hozni
# Meg kell adni, hogy ez az endpoint milyen választ fig adni, a hívó felé
#Itt jön létre az adatbázis kapcsolat (generátor függvény)

@router.get("/", response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
async def get_products(db: AsyncSession = Depends(get_db)) -> list[Product]:
    return await list_products_service(db)

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def insert_product(product: ProductRequest, db: AsyncSession= Depends(get_db)) -> Product:
    return await insert_product_service(product, db)

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(product_id: str, db: AsyncSession= Depends(get_db)) -> Product:
    return await get_product_service(product_id, db)

@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product(product_id: str, 
                         product_update: ProductRequest, 
                         db: AsyncSession= Depends(get_db)) -> Product:
    return await update_product_service(product_id, product_update, db)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str,
                         db: AsyncSession= Depends(get_db)) -> None:
    await delete_product_service(product_id, db)
    return None
