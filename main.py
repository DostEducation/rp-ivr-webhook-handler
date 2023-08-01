import functions_framework
from google.cloud import tasks_v2
import os
import json

SERVICE_ACCOUNT_EMAIL = os.environ.get("SERVICE_ACCOUNT_EMAIL")
PROJECT = os.environ.get("GCP_PROJECT_NAME")
QUEUE = os.environ.get("GCP_QUEUE_NAME")
LOCATION = os.environ.get("GCP_RESOURCE_LOCATION")
TARGET_FUNCTION_URL = os.environ.get("TARGET_FUNCTION_URL")

@functions_framework.http
def handle(req):
    payload = json.dumps(req.get_json())
    client = tasks_v2.CloudTasksClient()
    parent = client.queue_path(PROJECT, LOCATION, QUEUE)
    task = {
        "http_request": { # Specify the type of request.
            "http_method": tasks_v2.HttpMethod.POST,
            "url": TARGET_FUNCTION_URL, # The full url path that the task will be sent to.
            "body": payload.encode('utf-8'),
            "headers": {"Content-type": "application/json"}
        }
    }

    response = client.create_task(request={"parent": parent, "task": task})
    print('Response we got from queue');
    print(response)
    return "Success"
