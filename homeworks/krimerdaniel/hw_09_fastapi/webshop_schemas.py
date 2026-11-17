from pydantic import BaseModel, Field
from datetime import datetime

#pydantic model

class StockRequest(BaseModel):

    item_name: str = Field(..., min_length=1)
    quantity: int
    unit_price: float

    category: str = ''


class StockResponse(StockRequest):

    item_id: str


class CustomerRequest(BaseModel):

    customer_name: str = Field(..., min_length=1)
    customer_email: str


class CustomerResponse(CustomerRequest):

    customer_id: str


class OrderRequest(BaseModel):

    customer_id: str = Field(..., min_length=1)
    item_id: str = Field(..., min_length=1)
    item_quantity: int = 1


class OrderResponse(OrderRequest):

    order_id: str
    order_time: datetime
    #customer_name: str
    #item_name: str
    order_value: float