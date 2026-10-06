from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool


class CreatePost(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    published: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
