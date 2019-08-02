import logging
import time

logger = logging.getLogger(__name__)


class Producer:
    async def handle(self):
        message = "Producing stuff"
        time.sleep(1)
        logger.debug(f"Sending: {message}")
        return message

    async def handler(self, websocket, path):
        while True:
            message = await self.handle()
            await websocket.send(message)
