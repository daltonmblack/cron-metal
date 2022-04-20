from deta import app

from . import EnvData
from .email_utility import send_joke_email


@app.lib.cron()
def cron_job(event):
  try:
    env_data = EnvData()
    send_joke_email(env_data)
  except Exception as e:
    return f"Exception occurred: {e}"

  return "Email-triggering cron job completed successfully"
