# rp-ivr-webhook-handler
This repository codebase is responsible for enqueuing webhooks calls coming from RapidPro/KooKoo/other source to Cloud task.

Currently, there are issues with the number of inbound requests vs the system capabilities of handling those requests. 
So we are considering queues for handling the load. 
- When we will receive a webhook call, instead of calling the application database, we will queue the task to the cloud function. 
- Then the cloud function will trigger limited cloud function with a retry logic.

![Proposed implementation with queuing based implementation](https://user-images.githubusercontent.com/49094385/191035934-2ff17280-e076-4292-a5a3-f2a688cbef42.png)

- This will push limited number of requests to the webhook handler
- In case of a failed request, it will retry to push the request. Assuring that all the data are recorded.
