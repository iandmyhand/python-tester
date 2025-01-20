import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


from aws.ses import send_email


def send_email_via_ses():
    charset = "UTF-8"
    configuration_set = "my-configuration-set"  # Set up in AWS SES console
    sender = "sender@abc.com"  # Verified sender email that is set up in AWS SES
    recipient = "receiver@def.com"
    subject = "Test Email"
    sample_unsubscribe_token = "sampleToken"
    headers = {
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click",
        "List-Unsubscribe": f"<https://abc.com/unsubscribe/email/category/{sample_unsubscribe_token}>",
    }
    body_text = "This is a test email sent using Amazon SES with boto3."
    body_html = """
    <html>
    <head></head>
    <body>
    <h1>Test Email</h1>
    <p>This is sent using <b>Amazon SES</b> with boto3.</p>
    </body>
    </html>
    """
    # Message ID in the previous email sent result or received email.
    # If you want to send a new email, set thread_mail_message_id to None.
    thread_mail_message_id = "010c0194827de619-5d5b5847-b23e-4ec5-9c90-4b1d3147d80d-000000"
    thread_mail_message_id = None
    send_email(
        sender, recipient, charset, subject, body_text, body_html, configuration_set, headers, thread_mail_message_id
    )


if __name__ == "__main__":
    send_email_via_ses()
