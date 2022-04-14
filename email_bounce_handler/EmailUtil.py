import boto3
import ESLogger as eslogger


clientv2 = boto3.client('sesv2')

def add_to_suppression_list(emails):
    if emails is not None:
        for email in emails:
            response = clientv2.put_suppressed_destination(
                EmailAddress=email,
                Reason='BOUNCE'
            )
            eslogger.info('Adding ' + email + ' to suppression list')
            eslogger.info(response)
