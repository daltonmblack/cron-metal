import os
import pathlib
from os.path import exists

from cronmetal.email_utility import send_joke_email
from cronmetal.env_data import EnvData


def read_and_set_env_vars():
  base_dir = pathlib.Path(__file__).parent.resolve()
  env_file_path = base_dir.joinpath(".env")

  if not exists(env_file_path):
    raise Exception(f".env file missing from root project directory: {env_file_path}")

  with open(env_file_path, "r") as f:
    for line in f:
      if (not line) or (not line.strip()):
        continue

      line = line.strip()
      if line.startswith("#"):
        continue

      k, v = line.split("=", 1)
      os.environ[k] = v

def main():
  read_and_set_env_vars()

  env_data = EnvData()
  send_joke_email(env_data)

if __name__ == "__main__":
  main()
