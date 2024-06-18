from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/")
def api_root():
    return {"message": "Hello, you are on the API page"}
