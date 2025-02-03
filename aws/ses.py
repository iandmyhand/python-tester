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
import re

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def send_email(
    sender: str,
    recipients: list[str],
    charset: str,
    subject: str,
    body_text: str,
    body_html: str,
    configuration_set: str,
    headers: dict[str] | None,
    thread_mail_message_id: str | None,
):
    """Send an email using Amazon SES.
    Args:
        sender (str): The email address that sends the email.
        recipients (list[str]): The email addresses that receive the email.
        headers (dict): Additional headers to include in the email.
            If you want to put Gmail's One-Click Unsubscribe button in the Gmail client,
            you should setup SPF, DKIM, and DMARC for your domain.
            Please refer below link:
            https://support.google.com/a/answer/81126?hl=en&sjid=3499273166262528914-NC#requirements-5k&zippy=Crequirements-for-sending-or-more-messages-per-day
            Also, you should add the List-Unsubscribe-Post and List-Unsubscribe headers.
            Example:
            {
                "List-Unsubscribe-Post": "List-Unsubscribe=One-Click",
                "List-Unsubscribe": f"<https://yourdomain.com/unsubscribe/{UNSUBSCRIBE_TOKEN}>",
                ...
            }
        charset (str): The character encoding for the email.
        subject (str): The subject of the email.
        body_text (str): The plain text content of the email.
        body_html (str): The HTML content of the email.
        configuration_set (str): The name of the configuration set to use when sending the email.
            It must be configured in advance in the AWS SES console.
        thread_mail_message_id (str): The message ID of the email to which the email is a reply.
            If None, the email is not a reply.
            You can get the message ID from previous emails sent using Amazon SES.
            In the response, look for the "MessageId" key.
            This shouldn't be the same as the "Message-ID" header in the previous sent email.
            If you put the Gmail's message ID, it will be threaded with the message ID in Gmail.
            So you can choose the message ID that you want to thread with.
            Just you need to care about the format of the message ID,
            it should be ended with domain like this: MESSAGE_ID@address.com
    """
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["ReplyToAddresses"] = sender
    if thread_mail_message_id:
        if not subject.startswith("Re:"):
            msg["Subject"] = f"Re: {subject}"
        else:
            msg["Subject"] = subject
        if not contains_email_address(thread_mail_message_id):
            msg["In-Reply-To"] = f"{thread_mail_message_id}@ap-northeast-2.amazonses.com"
            msg["References"] = f"{thread_mail_message_id}@ap-northeast-2.amazonses.com"
        else:
            msg["In-Reply-To"] = f"{thread_mail_message_id}"
            msg["References"] = f"{thread_mail_message_id}"
    else:
        msg["Subject"] = subject
    if headers:
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
            Destinations=recipients,
            RawMessage={
                "Data": raw_message.read(),
            },
            ConfigurationSetName=configuration_set,
        )
        print("Email sent! Message ID:", response)
    except NoCredentialsError:
        print("AWS credentials not found.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials provided.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def contains_email_address(message_id):
    # Regular expression for standard email address
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.search(pattern, message_id) is not None
