from fastapi import FastAPI

app = FastAPI(title="Provify FastAPI Test")

@app.get("/")
async def root():
    return {"message": "FastAPI Provify Test"}

@app.get("/health")
async def health():
    return {"status": "ok"}
