import json
import os

class CallRepository:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_dir, '../data/seed_data.json')

    def get_all_calls(self):
         try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
         except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []