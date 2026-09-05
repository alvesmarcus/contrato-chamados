from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal


app = FastAPI(
    title="API de Chamados de Suporte",
    version="1.0.0"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/chamados", response_model=schemas.ChamadoResponse, status_code=201)
def criar_chamado(chamado: schemas.ChamadoCreate, db: Session = Depends(get_db)):
    return crud.criar_chamado(db, chamado)


@app.get("/chamados", response_model=list[schemas.ChamadoResponse])
def listar_chamados(db: Session = Depends(get_db)):
    return crud.listar_chamados(db)


@app.get("/chamados/{id}", response_model=schemas.ChamadoResponse)
def buscar_chamado(id: int, db: Session = Depends(get_db)):
    chamado = crud.buscar_chamado(db, id)

    if chamado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado."
        )

    return chamado