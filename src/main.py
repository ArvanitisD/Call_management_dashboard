from fastapi import FastAPI
# Κάνουμε import ΜΟΝΟ τον router. Αυτός αναλαμβάνει τα υπόλοιπα.
from routers.calls import router as calls_router

app = FastAPI(title="Call Management Dashboard")

# Συνδέουμε τον router των calls
app.include_router(calls_router)

@app.get("/")
def root():
    return {"message": "Welcome to Call Management API. Go to /calls to see data!"}