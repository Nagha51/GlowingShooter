import logging

logger = logging.getLogger(__name__)


class Consumer:
    async def handle(self, message):
        logger.debug(f"Handling {message}")
        return "ACK: " + message

    async def handler(self, websocket, path):
        async for message in websocket:
            await self.handle(message)
