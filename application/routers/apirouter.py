from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from ..services.consumeService import Consumer

class RequestParams(BaseModel):
    method: str
    service_type: str
    url: str
    headers: Optional[dict] = None
    body: Optional[str] = None

router = APIRouter(prefix="/rest-api/v1")

@router.post("/consume", status_code=200)
def consume(params: RequestParams):
    print("Consuming: " + params.url)
    return Consumer.consumeService(params.dict())