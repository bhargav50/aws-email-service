import json

import MultiThreadedEmailSender as email_sender
import QueueUtil as queue_util
import ESLogger as eslogger


""" Event Bridge Trigger """
def lambda_handler_sqs(event, context):
    messages = queue_util.get_messages()
    if len(messages) == 0:
        eslogger.info("No messages found in queue")
    else:
        eslogger.info("Received messages count : " + str(len(messages)))
        email_sender.process_messages(messages);

    return get_response_from_input(event)


def get_response_from_input(event):
    response = {}
    if event is not None and 'iteration_count' in event:
        response = {
            'iteration_count': event['iteration_count'],
            'iteration_max_count': event['iteration_max_count']
        }
    return response
