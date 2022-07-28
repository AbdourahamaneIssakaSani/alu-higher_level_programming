#!/usr/bin/python3
"""Are you docuemnted ?"""

def save_to_json_file(my_obj, filename):
    """How far now"""
    with open(filename, "w+") as f:
        return json.dump(my_obj, f)
