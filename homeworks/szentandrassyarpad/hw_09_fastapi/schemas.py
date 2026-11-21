# ez is modell, a request formátuma,ill a válaszban is milyen mezők legyenek.
from pydantic import BaseModel, Field
from decimal import Decimal

#pydantic model,nem adatbázis model. Eltérő formátumú a request és a response. 
# Az id a requestben nincs benne, a response-ban viszont igen

class ItemRequest(BaseModel):

    item_name: str = Field(..., min_length=1) # a item_name-t kötelező megadni a requestben, és legalább 1 karakter hiosszú legyen
    quantity:  int
    price:  Decimal
    category: str

class ItemResponse(ItemRequest): # ugyanaz mint a ItemRequest, ezért őt örökli, + az id
    # mivel data class, nem kell super -rel vacakolni

    id: str


