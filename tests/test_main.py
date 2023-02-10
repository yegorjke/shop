import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from shop.main import create_app

pytestmark = pytest.mark.asyncio


async def test_create_app():
    app = await create_app()
    assert isinstance(app, FastAPI)


async def test_index_route(client: AsyncClient):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json()["version"] == "1.0"  # TODO: move to settings
