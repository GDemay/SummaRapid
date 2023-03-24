import logging
import os
from dotenv import load_dotenv
import httpx

from app.core.settings import Settings


class reCAPTCHA():
    def __init__(self):
        self.settings = Settings()
        self.recaptcha_secret_key  = self.settings.recaptcha_secret_key
        if not self.recaptcha_secret_key:
            raise ValueError("The reCAPTCHA secret key cannot be empty")


    async def verify_recaptcha(self, captcha_response: str) -> bool:
        is_local = self.settings.environment.value == "local"
        if is_local:
            logging.warn("Local environment, skipping captcha verification")
            return True
        verify_url = "https://www.google.com/recaptcha/api/siteverify"
        payload = {"secret": self.recaptcha_secret_key, "response": captcha_response}

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(verify_url, data=payload)
        except httpx.RequestError as e:
            logging.error(f"An error occurred while verifying the captcha: {e}")
            return False
        except httpx.HTTPStatusError as e:
            logging.error(f"An error occurred while verifying the captcha: {e}")
            return False
        except httpx.TimeoutException as e:
            logging.error(f"An error occurred while verifying the captcha: {e}")
            return False
        logging.info(response.text)
        return response.status_code == 200