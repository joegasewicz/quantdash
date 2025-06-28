import asyncio
import tornado

from quantdash.routes import HealthHandler


class Server:

    port: int

    app: tornado.web.Application

    def __init__(self, *, port=8888):
        self.port = port
        self.app = self._create_app()

    def _create_app(self) -> tornado.web.Application:
        return tornado.web.Application([
            (r"/health", HealthHandler),
        ])

    async def create(self):
        self.app.listen(port=self.port)
        await asyncio.Event().wait()

    def run(self):
        asyncio.run(self.create())
