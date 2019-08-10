import argparse
from glowing_shooter.server.core.flaskio_server import run as flaskio_run
from glowing_shooter.server.core.logger import configure_logger


def configure_parser():
    parser = argparse.ArgumentParser(description="Start your server")
    parser.add_argument("--host", dest="host", required=False, help="Hostname", default="127.0.0.1", type=str)
    parser.add_argument("--port", dest="port", required=False, help="Port", default=8080, type=int)
    return parser


def start_server():
    parser = configure_parser()
    logger = configure_logger()

    logger.debug("Parsing inputs")
    parsed_args = parser.parse_args()

    logger.debug("Starting game")
    flaskio_run(parsed_args.host, parsed_args.port, logger)


if __name__ == "__main__":
    start_server()
