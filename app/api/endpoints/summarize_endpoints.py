from fastapi import APIRouter
from app.api.models.summarize_models import SummarizeModel
from app.api.services.summarize_service import SummarizeService

summarize_router = APIRouter()

@summarize_router.get("/")
def index():
    return {"Hello": "World from summarize"}

@summarize_router.post("/summarize")
async def create_summarize_content(text_to_summarize:str, max_length: int):
	summarize_service =  SummarizeService()
	summarize_content = summarize_service.summarize_text(text_to_summarize=text_to_summarize, max_length=max_length)
	return {"Summarize content": summarize_content}

@summarize_router.get("/users/{user_id}")
def read_item(user_id: int):
    return {"user_id": user_id}