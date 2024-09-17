# src/utils.py

import json

def format_as_json(data):
    return json.dumps(data, indent=4)