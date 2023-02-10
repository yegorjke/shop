import asyncio

import pytest
import pytest_asyncio
from httpx import AsyncClient

from shop.main import create_app

BASE_URL = "http://localhost:8001/api/"


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def app():
    _app = await create_app()
    yield _app


@pytest_asyncio.fixture
async def client(app):
    async with AsyncClient(app=app, base_url=BASE_URL, follow_redirects=True) as _client:
        yield _client
