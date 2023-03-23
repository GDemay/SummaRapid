from fastapi import APIRouter, HTTPException, Query
from app.api.models.summarize_models import SummarizeModel
from app.api.services.google_captcha import reCAPTCHA
from app.api.services.summarize_service import SummarizeService

summarize_router = APIRouter()


@summarize_router.get("/")
def index():
    print("State: Online")
    return {"State": "Online"}


@summarize_router.post("/summarize")
async def create_summarize_content(
    text_to_summarize: str = Query(..., min_length=1, description="The text to be summarized"),
    captcha: str = Query(..., description="The reCAPTCHA response")):
    """
    Summarize a given text.

    This endpoint receives a text and returns a summarized version of the content.

    Parameters:
    - text_to_summarize (str): The input text to be summarized.

    Returns:
    - dict: A dictionary containing the summarized content.
    """
    print("Starting Captcha check")
    recaptcha = reCAPTCHA()

    is_valid_captcha = await recaptcha.verify_recaptcha(captcha)
    if not is_valid_captcha:
        print("Invalid reCAPTCHA response")
        raise HTTPException(status_code=400, detail="Invalid reCAPTCHA response")

    print("Captcha check passed")
    summarize_service = SummarizeService()
    summarize_content = summarize_service.summarize_text(text_to_summarize=text_to_summarize)
    return {"summarized_content": summarize_content}