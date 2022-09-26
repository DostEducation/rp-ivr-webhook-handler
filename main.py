import functions_framework
from google.cloud import tasks_v2
import os

SERVICE_ACCOUNT_EMAIL = os.environ.get("SERVICE_ACCOUNT_EMAIL")
PROJECT = os.environ.get("GCP_PROJECT_NAME")
QUEUE = os.environ.get("GCP_QUEUE_NAME")
LOCATION = os.environ.get("GCP_RESOURCE_LOCATION")
TARGET_FUNCTION_URL = os.environ.get("TARGET_FUNCTION_URL")
TASK_NAME = os.environ.get("GCP_QUEUE_NAME") + "_task"

@functions_framework.http
def handle(req):
    payload = req.get_json()
    if payload is None:
        return False
        # handle this case

    client = tasks_v2.CloudTasksClient()
    parent = client.queue_path(PROJECT, LOCATION, QUEUE)
    task = {
        "http_request": {
            "http_method": tasks_v2.HttpMethod.POST,
            "url": TARGET_FUNCTION_URL,
            "body": payload.encode(),
            "headers": {"Content-type": "application/json"}
        }
    }
    task["name"] = client.task_path(PROJECT, LOCATION, QUEUE, TASK_NAME)

    response = client.create_task(request={"parent": parent, "task": task})
    return response
