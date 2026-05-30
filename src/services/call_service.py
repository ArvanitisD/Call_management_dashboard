from src.repositories.call_repository import CallRepository

# Create the CallService class that will use the CallRepository to perform operations on calls
class CallService:
    
    def __init__(self, repository=None):
        self.repository = repository if repository is not None else CallRepository()



    def get_all_calls(self):
        calls = self.repository.get_all_calls()
        filtered_calls = []
        for call in calls:
            if not call["is_archived"]:
                filtered_calls.append(call)
        return filtered_calls



    def get_call_by_id(self, call_id):
        return self.repository.get_call_by_id(call_id)



    def archive_call(self, call_id):
        call = self.repository.get_call_by_id(call_id)
        if call:
            call["is_archived"] = True
            return call
        return None
    


    def unarchive_call(self, call_id):
        call = self.repository.get_call_by_id(call_id)
        if call:
            call["is_archived"] = False
            return call
        return None



    def delete_call(self, call_id):
        return self.repository.delete_call(call_id)
         