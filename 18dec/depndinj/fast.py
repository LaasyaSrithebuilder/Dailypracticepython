from fastapi import FastAPI, Depends
from dep2 import Server, Database

app = FastAPI()

def get_database():
    return "Database connection setup"

@app.get("/data")
def read_data(db: str = Depends(get_database)):
    server = Server(Database())
    return {"data": server.getdata()}