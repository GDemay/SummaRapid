from fastapi import FastAPI
from pydantic import BaseModel


class SummarizeModel(BaseModel):
  	text: str