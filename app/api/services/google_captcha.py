import os
from dotenv import load_dotenv
import httpx


class reCAPTCHA():
	def __init__(self):
		load_dotenv()
		self.recaptcha_secret_key  = os.getenv("RECAPTCHA_SECRET_KEY")
		if not self.recaptcha_secret_key:
			raise ValueError("The reCAPTCHA secret key cannot be empty")


	async def verify_recaptcha(self, captcha_response: str) -> bool:
		is_development = os.getenv("ENVIRONNMENT") == "development"
		if is_development:
			print("Local development environment, skipping captcha verification")
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