import json

import EmailSender as email_sender
import QueueUtil as queue_util
import ESLogger as eslogger
from botocore.exceptions import ClientError


""" Event Bridge Trigger """
def lambda_handler_sqs(event, context):
    messages = queue_util.get_messages()
    if len(messages) == 0:
        eslogger.info("No messages found in queue")
    else:
        eslogger.info("Received messages count : " + str(len(messages)))

    failed_messages = []
    for message in messages:
        eslogger.info(message)
        body = message['Body']
        payload = json.loads(body)
        try:
            response = email_sender.send_email(payload)
            queue_util.delete_message(message)
        except ClientError as e:
            eslogger.error(e)
            failed_messages.append(message)

    if len(failed_messages) > 0:
        eslogger.info("Failed message count : " + str(len(failed_messages)))

    return {}
