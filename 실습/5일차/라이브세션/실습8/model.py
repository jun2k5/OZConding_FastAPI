from pydantic import BaseModel, field_validator, Field
from datetime import datetime

class Reservation(BaseModel):
    name: str # = Field( ... , max_length=50, description="최대입력길이는 50자")
    email: str
    date: datetime
    special_requests: str = Field(default="")

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if len(value) > 50:
            raise ValueError("50자 이내로 입력")
        return value
    
    @field_validator("date")
    @classmethod
    def validate_name(cls, value):
        if value < datetime.now():
            raise ValueError("미래 시간으로 예약")
        return value
    


