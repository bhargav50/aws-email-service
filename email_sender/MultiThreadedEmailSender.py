import json
import threading
from botocore.exceptions import ClientError

import ESLogger as eslogger
import EmailSender as email_sender
import QueueUtil as queue_util


def process_messages(messages):
    failed_messages = []
    threads = []
    for message in messages:
        # send_email(message, failed_messages)
        thread = threading.Thread(target=send_email, args=(message,failed_messages,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if len(failed_messages) > 0:
        eslogger.info("Failed message count : " + str(len(failed_messages)))


def send_email(message, failed_messages):
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
        failed_messages.append(message)
