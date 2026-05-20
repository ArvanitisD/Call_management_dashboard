from fastapi import APIRouter
from services.call_service import CallsService

router = APIRouter(prefix="/calls", tags=["calls"])

@router.get("/")
def get_calls():
    service = CallsService()
    
    return service.get_all_calls()