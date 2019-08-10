from flask import render_template, send_from_directory
from config.default import assets_path

from glowing_shooter.server.core.flaskio_server import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<path:filename>")
def serve_static_file(filename: str):
    return app.send_static_file(filename)


@app.route("/assets/<path:filename>")
def serve_assets_file(filename: str):
    return send_from_directory(assets_path, filename)
