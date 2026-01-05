from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field( ... , gt=0, description="Price must be greater than 0")
    description: str = "No description"




