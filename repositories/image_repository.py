from fastapi import UploadFile
from io import BytesIO
from PIL import Image
from typing import List

class ImageRepository:
    async def process_image(self, image: UploadFile) -> Image.Image:
        """
        Read an uploaded image file and convert it to a PIL Image object
        """
        image_bytes = await image.read()
        return Image.open(BytesIO(image_bytes))
        
    async def get_images_from_files(self, files: List[UploadFile]) -> List[Image.Image]:
        """
        Process multiple image files and return a list of PIL Images
        """
        images = []
        for file in files:
            image = await self.process_image(file)
            images.append(image)
        return images