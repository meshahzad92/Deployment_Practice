import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Railway!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use Railway's assigned PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
