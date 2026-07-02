from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI(title="Phishing Email Detection")


@app.get("/", response_class=HTMLResponse)
def read_root():
    index_path = Path(__file__).parent / "templates" / "index.html"
    return index_path.read_text(encoding="utf-8")
