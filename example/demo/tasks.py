import asyncio
import random

import logging

__all__ = ["aio_task_test"]
logger = logging.getLogger("default")


async def aio_task_test(app):
    i = 0
    while True:
        sleep_time = random.randrange(3, 7)
        # print('Hello world! (sleep: %s)(i: %s)' % (sleep_time, i))
        logger.info('Hello world! (sleep: %s)(i: %s)' % (sleep_time, i))
        await asyncio.sleep(sleep_time)
        # print('Hello again! (sleep: %s)(i: %s)' % (sleep_time, i))
        logger.info('Hello again! (sleep: %s)(i: %s)' % (sleep_time, i))
        i += 1
