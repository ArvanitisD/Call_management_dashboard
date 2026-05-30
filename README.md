# Call Management Dashboard API

![CI](https://github.com/ArvanitisD/Call_management_dashboard/actions/workflows/ci.yml/badge.svg)

A backend API for managing call records. Built with FastAPI and Python.



## What it does 
This API handles call records stored in a JSON file. You can fetch all active calls, look up a specific one by ID, archive it, or delete it.



## Tech Stack 
- Python          : Core language 
- FastAPI         : Framework
- pytest          : Testing
- httpx           : Required by FastAPI's TestClient
- GitHub Actions  : Runs tests automatically on every push



## Installation

### 1. Clone the repository
\```bash
git clone https://github.com/ArvanitisD/Call_management_dashboard.git
\```

### 2. Create virtual environment
\```bash
python -m venv venv
source venv/Scripts/activate
\```

### 3. Install dependencies
\```bash
pip install -r requirements.txt
\```

### 4. Run the app
\```bash
uvicorn src.main:app --reload
\```


## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/calls` | Get all calls (archived ones are excluded) |
| GET | `/calls/{id}` | Get one call by ID |
| PATCH | `/calls/{id}/archive` | Archive a call |
| DELETE | `/calls/{id}` | Delete a call |


## Features

- Get all calls, with archived ones filtered out automatically
- Get a call by ID
- Archive a call
- Delete a call
- Tests for every endpoint
- CI pipeline that runs on every push
- Deployment with Vercel



## Known Limitations
Data lives in a JSON file, so it resets every time the server restarts. There's no authentication either, so all endpoints are public. No pagination, so if the dataset grows large, performance will take a hit.


Given more time, I'd add PostgreSQL for persistent storage, JWT authentication, and pagination. I would also add additional functions, endpoints, and write unit tests for the service and repository layers, not just integration tests for the routes.
