import os
import boto3

sns_client = boto3.client(
    "sns",
    aws_access_key_id=os.environ.get("AMAZON_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AMAZON_SECRET_ACCESS_KEY"),
    region_name=os.environ.get("AMAZON_SNS_REGION_NAME"),
)


def send_sms(phone_number, message):
    smsattrs = {
        "AWS.SNS.SMS.SenderID": {"DataType": "String", "StringValue": "BPET"},
        "AWS.SNS.SMS.SMSType": {
            "DataType": "String",
            "StringValue": "Promotional",
        },
    }

    response = sns_client.publish(
        PhoneNumber=phone_number, Message=message, MessageAttributes=smsattrs
    )

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return True
    return False
