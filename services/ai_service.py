import google.generativeai as genai
from fastapi import UploadFile
from typing import List
from PIL import Image
from config.settings import Settings

class AIService:
    def __init__(self):
        settings = Settings()
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(model_name='gemini-2.0-flash')
        self.default_prompt = "Give the text from the image that has been provided. No preamble text and any other text. Keep only text from the image, no other text."
    
    def extract_text_from_image(self, image: Image.Image) -> str:
        """
        Extract text from a single image using Gemini AI
        """
        response = self.model.generate_content([self.default_prompt, image])
        return response.text