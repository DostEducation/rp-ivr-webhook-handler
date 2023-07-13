import functions_framework
from google.cloud import tasks_v2
import json, config
from utils.api import requires_api_token

@functions_framework.http
@requires_api_token
def handle(request):
    payload = json.dumps(request.get_json())
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
    print('Response we got from queue')
    print(response)
    return "Success"
