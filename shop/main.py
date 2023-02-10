from fastapi import APIRouter, FastAPI

from shop.api.index import router as index


async def create_app():
    app = FastAPI()
    router = APIRouter(prefix="/api")

    router.include_router(index)
    app.include_router(router)

    return app
