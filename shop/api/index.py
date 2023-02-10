from fastapi.routing import APIRouter

router = APIRouter(tags=["index"])


@router.get("/")
async def index():
    return {"version": "1.0"}
