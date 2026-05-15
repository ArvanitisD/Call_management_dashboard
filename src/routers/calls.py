from fastapi import APIRouter 

router = APIRouter()

@router.get("/calls")
def get_calls():
    return {"message": "Success"}