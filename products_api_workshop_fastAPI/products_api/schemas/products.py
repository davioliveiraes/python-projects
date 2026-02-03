from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    price: Decimal
    description: str

class ProductPublicSchema(BaseModel):
    id: int
    name: str
    price: Decimal
    description: str

class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    description: Optional[str] = None

class ProductListPublicSchema(BaseModel):
    products: List[ProductPublicSchema]
