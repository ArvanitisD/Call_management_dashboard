from fastapi import FastAPI
from routers.calls import router as calls_router

app = FastAPI(title="Call Management Dashboard")

# Connect the calls router to the main app
app.include_router(calls_router)

@app.get("/")
def root():
    return {"message": "Welcome to Call Management API. Go to /calls to see data!"}