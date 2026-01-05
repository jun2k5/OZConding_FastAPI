from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str
    quantity: int = Field(gt=1)

class Order(BaseModel):
    id: int
    items: list[Item]
    total_price: float = Field(gt=0)

    