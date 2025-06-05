import requests

MAILGUN_API_KEY = "34c0ebb96b470a6cee6d5147396841da-08c79601-f308256e"
MAILGUN_API_URL = "https://api.mailgun.net/v3/sandbox601169a1a37f47ce9438a20556738865.mailgun.org/messages"
FROM_EMAIL_ADDRESS = "postmaster@sandbox601169a1a37f47ce9438a20556738865.mailgun.org"

def send_email(to_address: str, subject: str, message: str):
    resp = requests.post(
        MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY),
        data={
            "from": FROM_EMAIL_ADDRESS,
            "to": to_address,
            "subject": subject,
            "text": message
        }
    )
    
    if resp.status_code == 200:
        print("Success! Email sent.")
        

send_email("hadinaufal06@gmail.com", "This is a test email", "This is a content message")