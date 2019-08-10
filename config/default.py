import os
import logging

this_dir = os.path.dirname(os.path.abspath(__file__))

dist_path = os.path.join(this_dir, "../dist")

assets_path = os.path.join(this_dir, "../assets")

UPDATE_EVENT = "update"

TICKRATE_MS = 100
TICKRATE_SEC = TICKRATE_MS / 1000

# Should match the name of the folder containing server code (allow logger inheritance/propagation)
BASE_LOGGER_NAME = "glowing_shooter"
BASE_LOGGER_LEVEL = logging.DEBUG
