import os


def retrieve_or_fail(env_var_name):
  val = os.getenv(env_var_name)
  if not val:
     raise Exception(f"Env var \"{env_var_name}\" required, but is missing or empty")

  return val

class EnvData:
  def __init__(self):
    self.sendgrid_api_key = retrieve_or_fail("SENDGRID_API_KEY")
    self.metal_jokes_api_url = retrieve_or_fail("METAL_JOKES_API_URL")
    self.from_email = retrieve_or_fail("FROM_EMAIL")
    self.to_emails = retrieve_or_fail("TO_EMAILS")
    self.template_id = retrieve_or_fail("TEMPLATE_ID")
