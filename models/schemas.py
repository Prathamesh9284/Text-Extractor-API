from pydantic import BaseModel
from typing import List, Optional

class ExtractionResponse(BaseModel):
    text: str
    
class ExtractionRequest(BaseModel):
    prompt: Optional[str] = "Give the text from the image that has been provided. No preamble text and any other text. Keep only text from the image, no other text."