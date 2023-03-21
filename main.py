from fastapi import FastAPI
import os
from app.api.endpoints.summarize_endpoints import summarize_router


stage = os.environ.get('STAGE', 'dev')

app = FastAPI()
app.include_router(summarize_router)
