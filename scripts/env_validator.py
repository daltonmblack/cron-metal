import pathlib
from os.path import exists

ENV_FILENAME = ".env"
TEMPLATE_FILENAME = ".env_TEMPLATE"


# Returns a sorted list of keys found in the file at env_file_path
def extract_keys(env_file_name):
  base_dir = pathlib.Path(__file__).parent.parent.resolve() # Project's root directory

  env_file_path = base_dir.joinpath(env_file_name)
  if not exists(env_file_path):
    raise Exception(f"Expected to find the {env_file_name} file in the root project directory")

  keys = []

  with open(env_file_path, "r") as f:
    for line in f:
      if (not line) or (not line.strip()):
        continue

      line = line.strip()
      if line.startswith("#"):
        continue

      k, _ = line.split("=", 1)
      keys.append(k)

  keys.sort() # This is an in-place operation

  return keys

def validate_keys():
  env_keys = extract_keys(ENV_FILENAME)
  template_keys = extract_keys(TEMPLATE_FILENAME)

  if env_keys != template_keys:
    raise Exception(f"Keys in {ENV_FILENAME} do not match keys in {TEMPLATE_FILENAME}")


if __name__ == "__main__":
  validate_keys()
