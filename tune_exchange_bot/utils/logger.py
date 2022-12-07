import logging
import os
from datetime import datetime

from tune_exchange_bot import PROJECT_PATH


logger = logging.getLogger(__name__)

log_dir = os.path.join(PROJECT_PATH, "logs")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

handler = logging.FileHandler(
    os.path.join(
        log_dir,
        f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    )
)

formatter = logging.Formatter(
    "%(asctime)s -  %(name)s: %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.INFO)
