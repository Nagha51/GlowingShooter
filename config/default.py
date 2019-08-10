import os
import logging

this_dir = os.path.dirname(os.path.abspath(__file__))

dist_path = os.path.join(this_dir, "../dist")

assets_path = os.path.join(this_dir, "../assets")

# EVENTS
PLAYER_UPDATE_EVENT = "update"
PLAYER_INPUT_EVENT = "input"

# SERVER CONFIGS
TICKRATE_MS = 100
TICKRATE_SEC = TICKRATE_MS / 1000

# Should match the name of the folder containing server code (allow logger inheritance/propagation)
BASE_LOGGER_NAME = "glowing_shooter"
BASE_LOGGER_LEVEL = logging.DEBUG
LOGGER_LEVEL_TRACE = 5

# GAME CONFIGS

PLAYER_HP = 100
PLAYER_SPEED = 400

MAP_SIZE = 3000
