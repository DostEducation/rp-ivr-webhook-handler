import functions_framework
from google.cloud import tasks_v2
from utils import logger
import config
import json


@functions_framework.http
def handle(req):
    try:
        payload = json.dumps(req.get_json())
        logger.info(f"Payload: {payload}")

        client = tasks_v2.CloudTasksClient()
        parent = client.queue_path(config.PROJECT, config.LOCATION, config.QUEUE)
        task = {
            "http_request": { # Specify the type of request.
                "http_method": tasks_v2.HttpMethod.POST,
                "url": config.TARGET_FUNCTION_URL, # The full url path that the task will be sent to.
                "body": payload.encode('utf-8'),
                "headers": {"Content-type": "application/json"}
            }
        }

        response = client.create_task(request={"parent": parent, "task": task})
        logger.info(f"Response from Cloud Tasks API: {response}")

        return "Success"
    except Exception as e:
        logger.error(f"Error in handle function: {e}")
