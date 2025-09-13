# src/ai_project/predict.py
from fastapi import APIRouter

from .schemas import PredictRequest, PredictResponse

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    # 簡單邏輯：輸入 * 2
    return PredictResponse(pred=payload.x * 2)
