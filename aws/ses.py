"""
Install boto3
$ pip install boto3

Set Up AWS Credentials
$ aws configure

Environment Variables:
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.generator import BytesGenerator
from io import BytesIO

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def send_email(sender, recipient, headers, charset, subject, body_text, body_html, configuration_set):
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = recipient
    msg["ReplyToAddresses"] = sender
    msg["Subject"] = subject
    for key, value in headers.items():
        msg[key] = value
    msg.attach(MIMEText(body_text, "plain", charset))
    msg.attach(MIMEText(body_html, "html", charset))

    raw_message = BytesIO()
    BytesGenerator(raw_message).flatten(msg)
    raw_message.seek(0)

    try:
        ses_client = boto3.client("ses", region_name="ap-northeast-2")
        response = ses_client.send_raw_email(
            Source=sender,
            Destinations=[
                recipient,
            ],
            RawMessage={
                "Data": raw_message.read(),
            },
            ConfigurationSetName=configuration_set,
        )
        print("Email sent! Message ID:", response["MessageId"])
    except NoCredentialsError:
        print("AWS credentials not found.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials provided.")
    except Exception as e:
        print(f"Failed to send email: {e}")
