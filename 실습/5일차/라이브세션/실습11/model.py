from pydantic import BaseModel, Field, model_validator
from datetime import datetime
import uuid

class User(BaseModel):
    user_id: str
    name: str
    role: str = Field(default="user")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    @model_validator
    def check_user_id(self):
        if not self.user_id:
            self.user_id = uuid.uuid4()


