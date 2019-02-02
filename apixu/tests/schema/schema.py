import os
import json


def read(filename):
    filename = os.path.dirname(os.path.realpath(__file__)) + "/" + filename
    with open(filename) as f:
        data = json.load(f)
        return data
