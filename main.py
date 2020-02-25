import json
import os
from parser import show_key_options

# change this variable to path for your json file
JSON_PATH = "nasa.json"


def main():
    """
    Body of the main program.
    """
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r") as f:
            nested_json = json.loads(f.read())
        if nested_json:
            show_key_options(nested_json, [])
    else:
        print("FATAL: NO JSON FILE FOUND.\nMake sure you changed JSON_PATH.")


if __name__ == "__main__":
    main()
