import os
from dotenv import load_dotenv
import httpx

from app.core.settings import Settings


class reCAPTCHA():
	def __init__(self):
		self.recaptcha_secret_key  = Settings.recaptcha_secret_key
		if not self.recaptcha_secret_key:
			raise ValueError("The reCAPTCHA secret key cannot be empty")


	async def verify_recaptcha(self, captcha_response: str) -> bool:
		is_local = Settings.environment.value == "local"
		if is_local:
			print("Local environment, skipping captcha verification")
			return True
		verify_url = "https://www.google.com/recaptcha/api/siteverify"
		payload = {"secret": self.recaptcha_secret_key, "response": captcha_response}

		try:
			async with httpx.AsyncClient() as client:
				response = await client.post(verify_url, data=payload)
		except httpx.RequestError as e:
			print(f"An error occurred while verifying the captcha: {e}")
			return False
		except httpx.HTTPStatusError as e:
			print(f"An error occurred while verifying the captcha: {e}")
			return False
		except httpx.TimeoutException as e:
			print(f"An error occurred while verifying the captcha: {e}")
			return False
		print(response.text)
		return response.status_code == 200