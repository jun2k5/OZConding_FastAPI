from pydantic import BaseModel, computed_field

class Product(BaseModel):
    name: str
    price: float
    discount: float

    @computed_field
    @property
    def final_price(self) -> float:
        return round(self.price * self.discount, 2)




