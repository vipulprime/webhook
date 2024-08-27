from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define the expected payload structure
class InBodyPayload(BaseModel):
    EquipSerial: str
    UserID: str
    Account: str

# Example header validation (optional)
# SECRET_KEY = "your_secret_key"

@app.post("/webhook")
async def inbody_webhook(payload: InBodyPayload, request: Request):
    # Optional: Validate the secret key in headers

    # Log the received payload for debugging
    print("Received Payload:", payload.dict())

    # Process the payload here (e.g., save to database, trigger other actions)
    
    # For this example, we'll just return a success message
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
