import json
import EmailUtil as email_util
import ESLogger as eslogger

def process_bounced_emails(records):
    bounced_emails = []
    for record in records:
        message = record['Sns']['Message']
        eslogger.info(" Message ")
        eslogger.info(message)
        message_dict = json.loads(message)
        bounced_recipients = message_dict['bounce']['bouncedRecipients']
        bounce_type = message_dict['bounce']['bounceType']
        for recipient in bounced_recipients:
            if bounce_type == 'Permanent':
                bounced_emails.append(recipient['emailAddress'])

    email_util.add_to_suppression_list(bounced_emails)
