import asyncio

LOOP = None

async def test_with_event_loop():
    global LOOP
    LOOP = asyncio.get_running_loop()
    assert asyncio.get_running_loop() is LOOP


def test_use_asyncio_run():
    async def check_loop():
        assert LOOP is not asyncio.get_running_loop()
    asyncio.run(check_loop())


async def test_event_loop_after_sync_run():
    assert LOOP is asyncio.get_running_loop()

