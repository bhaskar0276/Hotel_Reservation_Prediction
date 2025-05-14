import logging
import os
from datetime import datetime

LOGS_DIR='logs'



os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logging

logging.basicConfig(
    filename=LOG_FILE,  
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_logger(name):
    """
    Get a logger with the specified name.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger


