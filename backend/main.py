from fastapi import FastAPI
from model import gpt_model
from pydantic import BaseModel

class Query(BaseModel):
    query: str
    
app = FastAPI()

@app.get("/")
def read_root(query: str):
    return gpt_model.ask_the_model(query)
