import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_PATH = Path('data/logs/app.log')
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

handler = RotatingFileHandler(LOG_PATH, maxBytes=1_000_000, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)
logger.addHandler(handler)
