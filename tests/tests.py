""" Test """
import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app


@pytest.mark.asyncio()
async def test_hello() -> None:
    async with AsyncClient(
            transport=ASGITransport(app),
            base_url='http://test',
    ) as client:
        response = await client.get('/hello')
        assert response.status_code == 200
