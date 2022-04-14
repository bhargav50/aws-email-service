
import ESLogger as eslogger
import BounceHandler as bounce_handler


""" SNS Trigger """
def lambda_handler(event, context):

    eslogger.info("event :-")
    eslogger.info(event)

    if('Records' in event):
        records = event['Records']
        bounce_handler.process_bounced_emails(records)
