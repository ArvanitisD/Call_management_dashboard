import json 
from services.call_service import get_all_calls
from services.call_service import get_call_by_id
from services.call_service import archive_call

file_path = 'src/data/seed_data.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)


    all_calls = get_all_calls(data)
    print(all_calls)

    get_notes =get_call_by_id(data)
    print(get_notes)

    archive_calls = archive_call(data)
    print(archive_calls)

