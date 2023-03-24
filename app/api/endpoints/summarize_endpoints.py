import logging
from fastapi import APIRouter, HTTPException, Query
from app.api.models.summarize_models import SummarizeModel
from app.api.services.google_captcha import reCAPTCHA
from app.api.services.summarize_service import SummarizeService
from app.core.settings import settings
summarize_router = APIRouter()


@summarize_router.get("/")
def index():
    print("State: Online")
    logging.info("Application started with environment: %s", f"{settings.environment.value}")
    return {"State": "Online", "Environment": f"{settings.environment.value}]"}


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
    logging.info("Starting Captcha check")
    recaptcha = reCAPTCHA()

    is_valid_captcha = await recaptcha.verify_recaptcha(captcha)
    if not is_valid_captcha:
        logging.error("Invalid reCAPTCHA response")
        raise HTTPException(status_code=400, detail="Invalid reCAPTCHA response")

    logging.info("Captcha check passed")
    summarize_service = SummarizeService()
    summarize_content = summarize_service.summarize_text(text_to_summarize=text_to_summarize)
    logging.info({"Text": {text_to_summarize}, "Summarized content": {summarize_content}})
    return {"summarized_content": summarize_content}