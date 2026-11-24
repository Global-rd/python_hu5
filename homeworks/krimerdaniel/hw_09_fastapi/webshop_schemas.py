from pydantic import BaseModel, Field, EmailStr, ConfigDict
from decimal import Decimal
from datetime import datetime

#pydantic model

class StockRequest(BaseModel):

    product_id: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)


class StockResponse(StockRequest):

    stock_id: str


class ProductRequest(BaseModel):

    product_name: str = Field(..., min_length=1)
    manufacturer: str = Field(..., min_length=1)
    unit_price: Decimal = Field(..., ge=0, decimal_places=2)
    category: str = ''


class ProductResponse(ProductRequest):

    product_id: str


class CustomerRequest(BaseModel):

    customer_name: str = Field(..., min_length=1)
    customer_email: EmailStr


class CustomerResponse(CustomerRequest):

    customer_id: str


class OrderLineItemRequest(BaseModel):
    product_id: str = Field(..., min_length=1)
    item_quantity: int = Field(..., ge=1)


class OrderRequest(BaseModel):
    customer_id: str = Field(..., min_length=1)
    items: list[OrderLineItemRequest] = Field(..., min_length=1)


class OrderLineItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    itemline_id: str
    order_id: str
    product_id: str
    item_quantity: int
    order_value: float
    unit_price: float


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    order_id: str
    order_time: datetime
    customer_id: str
    items: list[OrderLineItemResponse]
    order_value: float