from flask import Flask
from flask_socketio import SocketIO
from config.default import dist_path
from glowing_shooter.server.core.game import Game
from glowing_shooter.server.core.background import background_thread

app = Flask(__name__)

socketio = SocketIO(app, logger=False)

game = Game()


def configure_app(curr_app):
    curr_app.template_folder = dist_path
    curr_app.static_folder = dist_path
    curr_app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def import_views():
    from glowing_shooter.server.views import http
    from glowing_shooter.server.views import sockets


def run(host: str, port: int, logger):
    logger.debug("Configuring flask app")
    configure_app(app)
    logger.debug("Importing views")
    import_views()
    logger.debug("Start background task")
    socketio.start_background_task(background_thread, socketio, game, logger=logger)
    print(f"Starting flaskio server on {host}:{port}")
    socketio.run(app, host=host, port=port)
