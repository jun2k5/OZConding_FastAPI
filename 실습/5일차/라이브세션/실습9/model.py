from pydantic import BaseModel, model_validator, EmailStr
import re

class ContactInfo(BaseModel):
    email: EmailStr | None = None
    phone_number: str | None = None

    @model_validator(mode="after")
    def check_input_email_phone_number(self):
        if self.email == None and self.phone_number == None:
            raise ValueError("이메일과 전화번호 중 하나는 입력해야합니다.")
        return self

    # @model_validator(mode="after")    
    # def check_email_pattern(self):
    #     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     if self.email and not re.match(pattern, self.email):
    #         raise ValueError("이메일형식에 맞춰주세요.")
    #     return self
    
    @model_validator(mode="before")
    @classmethod
    def check_email(cls, data):
        if isinstance(data, dict) and data.get("email"):
            data["email"] = data["email"].lower()
        return data










