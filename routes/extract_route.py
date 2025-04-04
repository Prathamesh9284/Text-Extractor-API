from fastapi import APIRouter, File, UploadFile
from typing import List
from services.image_service import ImageService

router = APIRouter(tags=["extraction"])

image_service = ImageService()

@router.get("/")
async def root():
    return {'message': 'Hello World!!!'}

@router.post('/extract-text')
async def extract_text(
    images: List[UploadFile] = File(...)
):
    return await image_service.extract_text_from_images(images)