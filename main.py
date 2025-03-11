import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Railway!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Ensure it uses the correct PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
