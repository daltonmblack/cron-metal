import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_joke_email(env_data):
  response = requests.get(env_data.metal_jokes_api_url)
  joke = response.json()["joke"]

  message = Mail(
    from_email=env_data.from_email,
    to_emails=env_data.to_emails,
  )
  message.dynamic_template_data = { "joke": joke }
  message.template_id = env_data.template_id
  
  sg = SendGridAPIClient(env_data.sendgrid_api_key)
  response = sg.send(message)
