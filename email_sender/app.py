import json

import EmailSender as email_sender


def lambda_handler(event, context):
    # Handling SQS request
    for record in event['Records']:
        payload = json.loads(record["body"])
        print(payload)
    email_sender.send_email(payload)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }


def lambda_handler_sqs(event, context):
    # Handling SQS request
    for record in event['Records']:
        payload = json.loads(record["body"])
        print(payload)
    email_sender.send_email(payload)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }


def get_email_dict(payload):
    email_dict = {}
    email_dict[""]
