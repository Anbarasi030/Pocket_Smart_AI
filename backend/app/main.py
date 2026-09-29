from fastapi import FastAPI

app = FastAPI(title="PocketSmart AI")


@app.get("/")
async def home():
    return {"message": "PocketSmart AI is running!"}