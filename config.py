"""Flask configuration."""
import os

FLASK_ENV = os.environ.get("FLASK_ENV", "development")

# Development env specific
if FLASK_ENV == "development":
    from os import path
    from dotenv import load_dotenv

    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))

SERVICE_ACCOUNT_EMAIL = os.environ.get("SERVICE_ACCOUNT_EMAIL")
PROJECT = os.environ.get("GCP_PROJECT_NAME")
QUEUE = os.environ.get("GCP_QUEUE_NAME")
LOCATION = os.environ.get("GCP_RESOURCE_LOCATION")
TARGET_FUNCTION_URL = os.environ.get("TARGET_FUNCTION_URL")
API_TOKEN = os.environ.get("API_TOKEN")
