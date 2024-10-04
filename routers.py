from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/home")
def home():
    return {"home":"home"}

