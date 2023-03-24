# from fastapi import FastAPI
# from mangum import Mangum

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from app.api.endpoints.summarize_endpoints import summarize_router
from app.core.logger_config import setup_logging


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_logging()
logging.info("FastAPI app started")
app.include_router(summarize_router)


handler = Mangum(app)
