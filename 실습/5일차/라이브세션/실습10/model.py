from pydantic import BaseModel, computed_field, field_validator

class Product(BaseModel):
    name: str
    price: float
    discount: float

    @field_validator("discount")
    @classmethod
    def validate_discount(cls, value):
        if not (0 < value < 100):
            raise ValueError("할인율은 0 ~ 100 사이 값이어야 합니다.")
        return value
    
    @computed_field
    @property
    def final_price(self) -> float:
        return round( self.price * (1 - self.discount / 100), 1)

