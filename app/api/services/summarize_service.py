import logging
import os
import openai
from dotenv import load_dotenv
import os
from app.core.settings import settings

class SummarizeService():
	def __init__(self):
		openai.api_key = settings.openai_api_key

	def summarize_text(self, text_to_summarize):
		if not text_to_summarize:
			raise ValueError("The text to summarize cannot be empty")
		response = openai.Completion.create(
			model="text-davinci-003",
			prompt=text_to_summarize + "\n\nTl;dr",
			temperature=0.7,
			max_tokens=200,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=1
			)

		summarized = response["choices"][0]["text"]
		print(f"Text to summarize:{text_to_summarize} summarized : {summarized}")
		return summarized