from fastapi import APIRouter, status

from views import generate_view

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello World"}


@router.post("/generate", status_code=status.HTTP_201_CREATED)
async def generate(body: dict):
    return generate_view(body)
