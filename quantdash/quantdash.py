from quantdash.server import Server
from quantdash.logger import logger


class QuantDash:

    server: Server

    def __init__(self):
        self.server = Server()

    def run(self):
        logger.info(f"Starting server on {self.server.port}")
        self.server.run()
