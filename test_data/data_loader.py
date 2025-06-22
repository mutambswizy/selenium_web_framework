# test_data/data_loader.py
import json
import os

def load_test_users():
    file_path = os.path.join(os.path.dirname(__file__), 'users.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['test_users']