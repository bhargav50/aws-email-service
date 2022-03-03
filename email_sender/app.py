import json

import EmailSender as email_sender
import ESLogger as eslogger

""" Handle messages from SQS """
def lambda_handler_sqs(event, context):
    # Handling SQS request
    for record in event['Records']:
        payload = json.loads(record["body"])
        print(payload)
    response = email_sender.send_email(payload)

    return response

""" Handle messages from SQS routed through SNS """
def lambda_handler_sns_sqs(event, context):
    eslogger.info("Received message from SQS --------")
    eslogger.info(event)

    for record in event['Records']:
        eslogger.info("Body of SQS payload ----")
        eslogger.info(record["body"])
        payload = json.loads(record["body"])
        eslogger.info("payload as dict ----")
        eslogger.info(payload)
        message = payload['Message']
        eslogger.info("Message from SNS payload ----")
        eslogger.info(message)
        email_dict = json.loads(message)
    response = email_sender.send_email(email_dict)

    return response
