import RegExUtil as regexutil

def get_to_be_suppressed_list(err_response):
    print("Printing error")
    print(err_response)
    print("Printing code")
    print(err_response['Error']['Code'])
    if (err_response['Error']['Code'] == "MessageRejected"):
        return regexutil.get_email_ids(err_response['Error']['Message'])




# {
#     'Error':
#     {
#         'Type': 'Sender',
#         'Code': 'MessageRejected',
#         'Message': 'Email address is not verified. The following identities failed the check in region US-EAST-2: strider.galaxie@gmail.com, merry.aru@gmail.com'
#     },
#     'ResponseMetadata': {
#         'RequestId': '056dde0b-9556-423e-82e7-76ff65cf95ba',
#         'HTTPStatusCode': 400,
#         'HTTPHeaders': {
#             'date': 'Sun, 27 Mar 2022 08:34:28 GMT',
#             'content-type': 'text/xml',
#             'content-length': '386',
#             'connection': 'keep-alive',
#             'x-amzn-requestid': '056dde0b-9556-423e-82e7-76ff65cf95ba'
#         },
#         'RetryAttempts': 0
#     }
# }
