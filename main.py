import functions_framework
from google.cloud import tasks_v2


@functions_framework.http
def handle_webhook(request):
    test = "hello world"
    return test
