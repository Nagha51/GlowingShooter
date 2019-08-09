import logging
import asyncio
import websockets

logger = logging.getLogger(__name__)


class Game:
    def __init__(self, consumer, producer, host="localhost", port=80):
        self.consumer = consumer
        self.producer = producer
        self.host = host
        self.port = port
        self.connected_users = set()

    async def register_user(self, websocket):
        logger.info(f"New user {websocket.remote_address[0]}:{websocket.remote_address[1]}")
        self.connected_users.add(websocket)

    async def unregister_user(self, websocket):
        logger.info(f"Lost user {websocket.remote_address[0]}:{websocket.remote_address[1]}")
        self.connected_users.remove(websocket)

    async def handler(self, websocket, path):
        await self.register_user(websocket)
        try:
            consumer_task = asyncio.ensure_future(
                self.consumer.handler(websocket, path))
            producer_task = asyncio.ensure_future(
                self.producer.handler(websocket, path))
            done, pending = await asyncio.wait(
                [consumer_task, producer_task],
                return_when=asyncio.FIRST_COMPLETED,
            )
            for task in pending:
                task.cancel()
        finally:
            await self.unregister_user(websocket)

    def start(self):
        logger.info(f"Starting server on {self.host}:{self.port}")
        return websockets.serve(self.handler, self.host, self.port)

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.start())
        logger.debug("Looping for everrrrr !")
        asyncio.get_event_loop().run_forever()
