from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = None


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     image: Optional[str] = None
#     tag: List[str] = []
    

# class Image(BaseModel):
#     url: HttpUrl
#     description: Optional[str] = None
    

# class Tag(BaseModel):
#     name: str
#     description: Optional[str] = None