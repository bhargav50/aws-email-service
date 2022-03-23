from datetime import datetime
import json
from unittest import TestCase
import boto3
import os
import uuid

SNS_TOPIC_ARN = os.getenv('SNS_TOPIC_ARN')

sns = boto3.client("sns")

def send_email(email_text):

    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=email_text,
        Subject="Testing Email Service from local",
        MessageGroupId=str(uuid.uuid4())
    )

    return response

class TestSNS(TestCase):
    def test_single_email(self):
        index = 0
        payload = dict()
        payload['from'] = 'bhargav@krinati.co'
        payload['to_addresses'] = ['bhargavsangani50@gmail.com']
        payload['title'] = 'Email Service ' + str(index)
        payload['body_html'] = '<h1> Just Testing</h1><p>Testing Email Service</p>'
        payload['body_text'] = 'Just Testing\nTesting Email Service'
        response = send_email(json.dumps(payload))
        expected_response = {
            'HTTPStatusCode': 200
        }
        self.assertEqual('ResponseMetadata' in response, True)
        received_metadata = response.get('ResponseMetadata')
        self.assertGreaterEqual(received_metadata.items(), expected_response.items())
        self.assertEqual(200, response.get('ResponseMetadata').get('HTTPStatusCode'))
