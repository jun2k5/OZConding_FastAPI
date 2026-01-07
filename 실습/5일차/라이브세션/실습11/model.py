from pydantic import BaseModel, Field, model_validator
from datetime import datetime
import uuid

class User(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    role: str = "user"
    created_at: datetime = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))






