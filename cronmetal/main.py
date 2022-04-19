import os

import requests
from deta import app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


@app.lib.cron()
def cron_job(event):
  send_joke_email()

  return "Hello, email-triggering cron!"


def send_joke_email():
  sendgrid_api_key = os.getenv("SENDGRID_API_KEY")

  if not sendgrid_api_key:
    return "Missing env var: SENDGRID_API_KEY"

  response = requests.get(os.getenv("METAL_JOKES_API_URL"))
  joke = response.json()["joke"]

  message = Mail(
    from_email=os.getenv("FROM_EMAIL"),
    to_emails=os.getenv("TO_EMAIL"),
  )
  message.dynamic_template_data = { "joke": joke }
  message.template_id = os.getenv("TEMPLATE_ID")
  try:
    sg = SendGridAPIClient(sendgrid_api_key)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
  except Exception as e:
    print(e.message)
