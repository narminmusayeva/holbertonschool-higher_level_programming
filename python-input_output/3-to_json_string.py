#!/usr/bin/python3
import json
def to_json_string(my_obj):
    """
    Returns the JSON representation

    Args:
    my_obj:The object to convert to JSON str

    Returns:
    str:JSON represantation of the object
    """
    return json.dumps(my_obj)
