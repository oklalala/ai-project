# src/ai_project/schemas.py
from pydantic import BaseModel


class PredictRequest(BaseModel):
    x: int  # 輸入數字
    multiplier: int = 2  # 預設乘數
    model_config = {"extra": "forbid"}  # 禁止多餘欄位


class PredictResponse(BaseModel):
    pred: int  # 輸出數字


class HealthCheckResponse(BaseModel):
    status: str  # 健康檢查狀態
