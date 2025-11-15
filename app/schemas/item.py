from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: str

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)