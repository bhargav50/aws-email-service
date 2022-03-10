import json

import EmailSender as email_sender
import ESLogger as eslogger


""" Handle messages from SQS"""
def lambda_handler_sqs(event, context):
    eslogger.info("Received message Batch from SQS --------")
    eslogger.info(event)

    eslogger.info("Batch size " + str(len(event['Records'])))
    for record in event['Records']:
        eslogger.info("Body of Message ----" + record['messageId'])
        eslogger.info(record["body"])
        payload = json.loads(record["body"])
        response = email_sender.send_email(payload)

    return response
