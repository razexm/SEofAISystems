from fastapi import FastAPI
from database import *
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/current-state/")
def get_current_state():
    db = SessionLocal()
    current_state = db.query(CurrentState).first()
    return {"state": current_state.state}

@app.get("/edges/")
def get_edges():
    db = SessionLocal()
    edges = db.query(Edges).filter(Edges.beginning == 0).all()  # Замените 0 на текущее состояние
    return [{"finish": edge.finish} for edge in edges]