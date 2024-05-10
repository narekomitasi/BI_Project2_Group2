import logging
from logging.handlers import RotatingFileHandler
import uuid
import os

# Ensuring the directory for logs exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Create logger
logger = logging.getLogger('RelationalDataFlowLogger')
logger.setLevel(logging.INFO)  # Adjust as needed

# Create handlers
handler = RotatingFileHandler('logs/logs_relational_data_pipeline.txt', maxBytes=10000, backupCount=5)
handler.setLevel(logging.INFO)

# Create formatter and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - execution_id=%(execution_id)s')
handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(handler)

# Adding the execution_id as an extra field to the logger
def log_message(level, msg):
    extra = {'execution_id': str(uuid.uuid4())}  # Generating a new UUID for each log entry
    if level.lower() == 'info':
        logger.info(msg, extra=extra)
    elif level.lower() == 'error':
        logger.error(msg, extra=extra)
    elif level.lower() == 'warning':
        logger.warning(msg, extra=extra)
    elif level.lower() == 'debug':
        logger.debug(msg, extra=extra)
