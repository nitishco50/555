from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from downloader import download_instagram_video

app = FastAPI(title="Instagram Downloader API")

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Production me apna domain dena
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DownloadRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Instagram Downloader API is running."
    }


@app.post("/download")
def download(data: DownloadRequest):
    return download_instagram_video(data.url)
