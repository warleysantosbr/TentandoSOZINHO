from fastapi import FastAPI
from database import Base, engine
from routes import aluno

app = FastAPI(title="API Escolar")

Base.metadata.create_all(bind=engine)

app.include_router(aluno.router)

@app.get("/")
def read_root():
    return {"mensagem": "API tá online malucooo 🔥"}