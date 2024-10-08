""" Test """
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio()
async def test_async() -> None:
    """Test"""
    client = AsyncClient()
    await client.get('https://yandex.ru/')
