from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from config.default import assets_path, dist_path


app = Flask(__name__)

socketio = SocketIO(app)

def configure_app(app):
    app.template_folder = dist_path
    app.static_folder = dist_path

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<path:filename>')
def serve_static_file(filename):
    return app.send_static_file(filename)

@app.route('/assets/<path:filename>')
def serve_assets_file(filename):
    return send_from_directory(assets_path, filename)

@socketio.on('connect')
def test_connect():
    print("Client connection")
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


def run(host, port):
    configure_app(app)
    print(f"Running flaskio server on {host}:{port}")
    socketio.run(app, host=host, port=port)
