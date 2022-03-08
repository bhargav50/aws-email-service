import json

import EmailSender as email_sender
import ESLogger as eslogger


""" Handle messages from SQS"""
def lambda_handler_sqs(event, context):
    eslogger.info("Received message from SQS --------")
    eslogger.info(event)

    for record in event['Records']:
        eslogger.info("Body of SQS payload ----")
        eslogger.info(record["body"])
        payload = json.loads(record["body"])
        eslogger.info("payload as dict ----")
        eslogger.info(payload)
    response = email_sender.send_email(payload)

    return response
