import logging
import config
from google.cloud import logging as gcloud_logging

logger = logging.getLogger()

if config.ENVIRONMENT == "development":
    logging.basicConfig(level=logging.DEBUG)
    log_handler = logger.handlers[0]
    logger.addHandler(log_handler)
else:
    logging.basicConfig(level=logging.INFO)
    log_client = gcloud_logging.Client()
    log_client.setup_logging()
    log_handler = log_client.get_default_handler()
    logger.addHandler(log_handler)
