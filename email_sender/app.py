import json

import EmailSender as email_sender
import QueueUtil as queue_util
import ESLogger as eslogger
import ErrorProcessor as error_processor
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
            eslogger.info("Printing error in handler")
            eslogger.error(e)
            eslogger.info("Printing error response in handler")
            eslogger.error(e.response)
            to_be_suppressed_list = error_processor.get_to_be_suppressed_list(e.response)
            email_sender.add_to_suppression_list(to_be_suppressed_list)
            failed_messages.append(message)

    if len(failed_messages) > 0:
        eslogger.info("Failed message count : " + str(len(failed_messages)))

    return get_response_from_input(event)


def get_response_from_input(event):
    response = {}
    if event is not None and 'iteration_count' in event:
        response = {
            'iteration_count': event['iteration_count'],
            'iteration_max_count': event['iteration_max_count']
        }
    return response
