import json
import os

class CallRepository:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(current_dir, '../data/seed_data.json')

        self.calls_data = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)                
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []


    def get_all_calls(self):
        return self.calls_data


    def get_call_by_id(self, call_id):
        for call in self.calls_data:
            if call["id"] == call_id:
                return call
        return None