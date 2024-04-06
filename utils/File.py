import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_DATA_DIR = os.path.join(ROOT_DIR, "testData")


def read_json(file_path):
    print("Reading json file from", file_path)
    with open(file_path, 'r') as file:
        return json.load(file)
