from typing import Annotated
from pydantic import BaseModel, Field
from meetifyr.dtos.frozen_config import FROZNEN_CONFIG

class CreateMeetingResponse(BaseModel):
    model_config = FROZNEN_CONFIG

    url_code: Annotated[str, Field(description="미팅 url 코드, unique 합니다.")]







