import json
from diflib import get_close_matches
def load_knowledge_base(file_path: str)-> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_pat)