import asyncio


async def test_an_async_test_is_required():
    """Without an async test, the error will not be raised"""
    pass


def test_run_async_in_new_loop():
    async def foo():
        pass
    asyncio.run(foo())

