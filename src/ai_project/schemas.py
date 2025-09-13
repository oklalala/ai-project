# src/ai_project/schemas.py
from pydantic import BaseModel


class PredictRequest(BaseModel):
    x: int  # 輸入數字


class PredictResponse(BaseModel):
    pred: int  # 輸出數字


class HealthCheckResponse(BaseModel):
    status: str  # 健康檢查狀態
