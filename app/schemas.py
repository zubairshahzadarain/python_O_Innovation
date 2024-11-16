from pydantic import BaseModel
from typing import List

class ImageResponse(BaseModel):
    depth: int
    color_image_base64: str
    image_shape: str  
