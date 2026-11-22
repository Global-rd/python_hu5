from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):

    # Basic product information
    item_name: str = Field(min_length=1, max_length=200)
    description: str | None = None
    category: str | None = None

    # Physical specifications
    scale: str | None = None
    height_cm: float | None = Field(default=None, gt=0)
    width_cm: float | None = Field(default=None, gt=0)
    depth_cm: float | None = Field(default=None, gt=0)
    material: str = "Resin"
    painted: bool = False

    # Pricing and availability
    price: float = Field(gt=0)
    quantity: int = Field(default=0, ge=0)
    made_to_order: bool = True
    production_days: int = Field(default=7, ge=0)

    # Product image and visibility
    image_url: str | None = None
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)