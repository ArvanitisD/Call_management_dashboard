from repositories.call_repository import CallRepository

from repositories.call_repository import CallRepository

# Create the CallService class that will use the CallRepository to perform operations on calls
class CallService:
    
    def __init__(self):
        self.repository = CallRepository()

    def get_all_calls(self):
        
        calls = self.repository.get_all_calls()
        filtered_calls = []
        for call in calls:
            if not call["is_archived"]:
                filtered_calls.append(call)
                
        return filtered_calls

    def get_call_by_id(self, call_id):
        calls = self.repository.get_all_calls()
        for call in calls:
            if call["id"] == call_id:
                return call
        return None

    def archive_call(self, call_id):
        calls = self.repository.get_all_calls()
        for call in calls:
            if call["id"] == call_id:
                call["is_archived"] = True
                return call
        return None

    def unarchive_call(self, call_id):
        calls = self.repository.get_all_calls()
        for call in calls:
            if call["id"] == call_id:
                call["is_archived"] = False
                return call
        return None
         
    def delete_call(self, call_id):
        calls = self.repository.get_all_calls()
        for call in calls:
            if call["id"] == call_id:
                calls.remove(call)
                return call
        return None
