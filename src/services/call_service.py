def get_all_calls(calls):
    # return all non-archived calls from the in-memory store

    filtered_calls = []
    for call in calls:
        if call["is_archived"] == False:
            filtered_calls.append(call)

    return filtered_calls


def get_call_by_id(call_id):
    # return a single call with its notes, or None if not found

    for call in call_id:
        if call == "note":
            return call
    return None

    

def archive_call(call_id):
    # set is_archived to True, return the updated call, or None if not found
    if "is_archived" == True:
        return call_id
    else:
        return None
    
