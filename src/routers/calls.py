from fastapi import APIRouter, HTTPException
from services.call_service import CallService

router = APIRouter(prefix="/calls", tags=["calls"])

@router.get("/")
def get_calls():
    service = CallService()
    
    return {"calls": service.get_all_calls()}

@router.get("/{call_id}")
def get_call(call_id: str):
    service = CallService()
    call = service.get_call_by_id(call_id)
    
    if not call:
        raise HTTPException(status_code=404, detail="Call not found")
    return call

@router.patch("/{call_id}/archive")
def archive_call(call_id: str):
    service = CallService()
    updated_call = service.archive_call(call_id)
    
    if not updated_call:
        raise HTTPException(status_code=404, detail="Call not found")
    return {"calls": updated_call}

@router.delete("/{call_id}")
def delete_call(call_id: str):
    service = CallService()
    deleted_call = service.delete_call(call_id)

    if not deleted_call:
        raise HTTPException(status_code=404, detail="Call not found")
    return {"calls": deleted_call}