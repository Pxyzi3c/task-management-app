import logging
import os

def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            # logging.FileHandler("app.log") # Uncomment for file logging
        ]
    )

    # Suppress chatty loggers
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)