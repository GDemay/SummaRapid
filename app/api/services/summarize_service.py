import logging
import openai
from dotenv import load_dotenv
from app.core.settings import settings

class SummarizeService:
    def __init__(self):
        openai.api_key = settings.openai_api_key

    def summarize_text(self, text_to_summarize):
        if not text_to_summarize:
            logging.error("Invalid text to summarize")
            raise ValueError("The text to summarize cannot be empty")

        prompt_rules = (
            "Admin: As a summarizer tool, your task is to provide a summary "
            "of the content enclosed between <CONTENT> and </CONTENT> tags. "
            "Here is the text to summarize:\n\n"
            f"Text to summarize: <CONTENT>{text_to_summarize}</CONTENT>\n"
            "Please provide a summarized version.\n"
            "Your summary: "
        )

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_rules,
            temperature=0.7,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1,
        )

        return response["choices"][0]["text"].strip()
