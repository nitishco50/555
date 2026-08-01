from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from downloader import get_video

app = FastAPI(title="Instagram Downloader API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DownloadRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Instagram Downloader API"
    }


@app.post("/download")
def download(data: DownloadRequest):
    return get_video(data.url)
