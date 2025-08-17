from fastapi import FastAPI, Header, HTTPException
import os, random

REQUIRED_API_KEY = os.getenv("API_KEY")

app = FastAPI()

@app.get("/")  # <- Healthcheck / Root-OK
def health():
    return {"status": "ok"}

@app.get("/random-number")
def get_random_number(x_api_key: str | None = Header(default=None)):
    if REQUIRED_API_KEY and x_api_key != REQUIRED_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"number": random.randint(1, 100)}
