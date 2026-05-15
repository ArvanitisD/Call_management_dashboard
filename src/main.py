import json 
from services.call_service import get_all_calls, get_call_by_id, archive_call, unarchive_call, delete_call 



file_path = 'src/data/seed_data.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)


    all_calls = get_all_calls(data)
    print(all_calls, "\n")

    get_notes =get_call_by_id(data, "4")
    print(get_notes, "\n")

    archive_calls = archive_call(data, "2")
    print(archive_calls, "\n")

    unarchive_calls = unarchive_call(data, "3")
    print(unarchive_calls, "\n")

    deleted_call = delete_call(data,"10")
    print(delete_call, "\n")

