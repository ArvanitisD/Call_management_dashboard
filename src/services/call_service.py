from repositories.call_repository import CallRepository

def get_all_calls(calls):
    # return all non-archived calls from the in-memory store

    filtered_calls = []
    for call in calls:
        if not call["is_archived"]:
            filtered_calls.append(call)

    return filtered_calls


def get_call_by_id(calls, call_id):
    # return a single call with its notes, or None if not found

    for call in calls:
        if call["id"] == call_id:
            return call
    return None

    

def archive_call(calls, call_id):
    # set is_archived to True, return the updated call, or None if not found

    for call in calls:
        if call["id"] == call_id:
            call["is_archived"] = True
            return call
    return None


def unarchive_call(calls, call_id):
    # set is_archived to False, return the updated call, or None if not found

    for call in calls:
        if call["id"] == call_id:
            call["is_archived"] = False
            return call
    return None
     

def delete_call(calls, call_id):
    # remove the call from the in-memory store, return the deleted call, or None if not found

    for call in calls:
        if call["id"] == call_id:
            calls.remove(call)
            return call
    return None        

# Create a service class to encapsulate the business logic
    def __init__(self):
        self.repository = CallRepository()

    def get_all_calls(self):
        return self.repository.get_all_calls()