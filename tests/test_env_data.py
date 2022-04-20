import os
from unittest import mock

import pytest
from cronmetal.env_data import EnvData


@mock.patch.dict(
  os.environ,
  {
    "SENDGRID_API_KEY": "PLACEHOLDER",
    "METAL_JOKES_API_URL": "PLACEHOLDER",
    "FROM_EMAIL": "PLACEHOLDER",
    "TO_EMAILS": "PLACEHOLDER",
    "TEMPLATE_ID": "PLACEHOLDER",
  },
  clear=True
)
def test_valid_environment():
  assert EnvData()

@mock.patch.dict(os.environ, { "SENDGRID_API_KEY": "PLACEHOLDER" }, clear=True) # Only set one key
def test_invalid_environment():
  with pytest.raises(Exception):
    EnvData()
