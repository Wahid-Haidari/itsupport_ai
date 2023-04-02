from fastapi import FastAPI
from model import gpt_model
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Query(BaseModel):
    query: str
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(query: str):
    return gpt_model.ask_the_model(query)
