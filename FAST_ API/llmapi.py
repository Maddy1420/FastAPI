from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
class RequestModel(BaseModel):
    name: str


@app.post("/generate")
def generate_text(request: RequestModel):
    # Placeholder implementation - replace with actual text generation logic
    return f"Welcome {request.name}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("llmapi:app", host="127.0.0.1", port=8000, reload = True)
