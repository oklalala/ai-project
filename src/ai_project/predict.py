# src/ai_project/predict.py
from fastapi import APIRouter

from .core import predict_value
from .schemas import PredictRequest, PredictResponse

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    # 簡單邏輯：輸入 * 2
    return PredictResponse(pred=predict_value(payload.x, payload.multiplier))
