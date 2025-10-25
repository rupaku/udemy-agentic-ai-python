from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

# port where ollama is running
client = Client(
    host="http://localhost:11434",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact-us")
def read_root():
    return {"email": "rupa.rk201@gmail.com"}

@app.post("/chat")
def chat(
        message: str = Body(..., description="The Message")
):
    response = client.chat(model="gemma:2b", messages=[
        { "role": "user", "content":message  }
    ])

    return { "response": response.message.content }