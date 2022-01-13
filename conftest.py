import asyncio
import pytest
import logging



@pytest.fixture(scope="session")
def event_loop(request):
    """
    Redefine the event loop to support session/module-scoped fixtures;
    see https://github.com/pytest-dev/pytest-asyncio/issues/68
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    
    try:
        yield loop
    finally:
        loop.close()
