# call-management-dashboard-Backend--Python-
My first Backend Python project

- In this project I built data layer and service logic for a call management dashboard, inspired by [Aircall](https://aircall.io/). 

--- FUNCTIONS ---

- get_all_calls(): Retrieves all non-archived (active) calls, ensuring the dashboard displays only relevant, ongoing activity.

- get_call_by_id(call_id): Fetches detailed information for a specific call, including associated notes, mirroring the "Call Details" view in Aircall.

- archive_call(call_id): Implements the archiving workflow by toggling the is_archived state, allowing users to declutter their feed without permanent data loss.

- delete_call(call_id): Provides the functionality to permanently remove call records from the data store.

If you want to see the results, run the main file of this project. 
