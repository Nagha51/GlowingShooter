import sys
import logging
import argparse
from glowing_shooter.server.core.flaskio_server import run as flaskio_run
from glowing_shooter.server.core.old_game import Game
from glowing_shooter.server.core.consumer import Consumer
from glowing_shooter.server.core.producer import Producer


def configure_parser():
    parser = argparse.ArgumentParser(description="Start your server")
    parser.add_argument("--host", dest="host", required=False, help="Hostname", default="127.0.0.1", type=str)
    parser.add_argument("--port", dest="port", required=False, help="Port", default=8080, type=int)
    return parser


def configure_logger():
    logger = logging.getLogger("glowing_shooter")
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    return logger


def start_server():
    logger = configure_logger()
    parser = configure_parser()
    logger.debug("Parsing inputs")
    parsed_args = parser.parse_args()

    consumer = Consumer()
    producer = Producer()
    game = Game(consumer, producer, **vars(parsed_args))
    logger.debug("Starting game")
    # game.run()
    flaskio_run(parsed_args.host, parsed_args.port)


if __name__ == "__main__":
    start_server()
