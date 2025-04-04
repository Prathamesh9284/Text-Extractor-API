from fastapi import UploadFile
from typing import List
from services.ai_service import AIService
from repositories.image_repository import ImageRepository

class ImageService:
    def __init__(self):
        self.image_repository = ImageRepository()
        self.ai_service = AIService()
    
    async def extract_text_from_images(self, image_files: List[UploadFile]) -> str:
        """
        Process multiple image files and extract text from them
        """
        extracted_text = ''
        
        for image_file in image_files:
            image = await self.image_repository.process_image(image_file)
            text = self.ai_service.extract_text_from_image(image)
            extracted_text += text
            
        return extracted_text