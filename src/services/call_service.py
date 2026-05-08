def get_all_calls():
    # return all non-archived calls from the in-memory store
    filtered_calls = []
    for call in seed_data:
        if not call["is_archived"]:
            filtered_calls.append()

    return filtered_calls

    pass

def get_call_by_id(call_id):
    # return a single call with its notes, or None if not found
    pass

def archive_call(call_id):
    # set is_archived to True, return the updated call, or None if not found
    if "is_archived" == True:
        return call_id
    else:
        return None
    pass
