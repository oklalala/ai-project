from fastapi import FastAPI

from .predict import router as predict_router

app = FastAPI(title="AI Project API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(predict_router)
