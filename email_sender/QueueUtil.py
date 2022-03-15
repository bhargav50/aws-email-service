import boto3
import os
import ESLogger as eslogger


sqs = boto3.client('sqs')

queue_url = os.getenv('EMAIL_SQS_QUEUE_URL','https://sqs.us-east-2.amazonaws.com/107569227309/email-sender-app-EmailSqsQueue-aMQc5YMCh1Ft.fifo')
# queue_url = os.getenv('EMAIL_SQS_QUEUE_URL')

def get_messages():

    eslogger.info("queue_url : ")
    eslogger.info(queue_url)
    messages = []
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        # VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    eslogger.info('Messages')
    eslogger.info(response)
    if 'Messages' in response:
        messages = response['Messages']
    return messages


def delete_message(message):
    receipt_handle = message['ReceiptHandle']
    eslogger.info("Deleting message from queue : messageId - " + message['MessageId'])
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    eslogger.info('Received and deleted message: %s' % message)
