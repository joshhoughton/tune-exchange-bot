
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)


if not os.path.exists("logs"):
    os.makedirs("logs")

handler = logging.FileHandler(os.path.join("logs", datetime.now().strftime('%Y%m%dT%H%M%S')))

formatter = logging.Formatter(
    "%(asctime)s -  %(name)s: %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.INFO)
