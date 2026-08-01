import instaloader

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_comments=False,
    save_metadata=False
)

def get_video(url: str):

    # Yahan baad me Instagram se metadata nikalne ka logic likhenge.

    return {
        "success": False,
        "message": "Downloader logic not implemented yet."
    }
