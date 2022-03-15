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
        eslogger.info('Body :')
        eslogger.info(body)
        payload = json.loads(body)
        try:
            response = email_sender.send_email(payload)
            queue_util.delete_message(message)
        except ClientError as e:
            eslogger.error(e)
            failed_messages.append(message)

    if len(failed_messages) > 0:
        eslogger.info("Failed message count : " + str(len(failed_messages)))



# """ Handle messages from SQS"""
# def lambda_handler_sqs(event, context):
#     eslogger.info("Received message Batch from SQS --------")
#     eslogger.info("Batch size " + str(len(event['Records'])))
#
#     failed_messages = []
#
#     for record in event['Records']:
#         eslogger.info("Body of Message ----" + record['messageId'])
#         eslogger.info(record["body"])
#         payload = json.loads(record["body"])
#         try:
#             response = email_sender.send_email(payload)
#         except ClientError as e:
#             failed_messages.append(record)
#
#     response = get_response(failed_messages)
#     eslogger.info("Response :- ")
#     eslogger.info(response)
#     return response


# """ Batch item failures are used by SQS to retry failed messages only from the batch"""
# def get_response(failed_messages):
#     response = {}
#     if len(failed_messages) > 0:
#         batch_items = []
#         for msg in failed_messages:
#             batch_items.append({"itemIdentifier": msg["messageId"]})
#         response["batchItemFailures"] = batch_items
#     return response
