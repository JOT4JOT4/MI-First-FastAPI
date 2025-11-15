from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class GameBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    image: Optional[str] = Field(None, max_length=1000)
    price: float = Field(..., ge=0)
    discount: Optional[float] = Field(None, ge=0, le=100)
    description: Optional[str] = Field(None, max_length=2000)

class GameCreate(GameBase):
    pass

class GameRead(GameBase):
    id: str

    model_config = ConfigDict(from_attributes=True)