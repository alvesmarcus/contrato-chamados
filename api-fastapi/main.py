from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI(
    title="API de Chamados",
    description="Primeira API de chamados utilizando FastAPI",
    version="1.0.0"
)


# Lista que funcionará como banco de dados em memória
chamados = []


# Modelo dos dados recebidos
class Chamado(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    status: str = "aberto"


@app.get("/")
def inicio():
    return {
        "mensagem": "API de Chamados funcionando!"
    }


@app.get("/chamados")
def listar_chamados():
    return chamados


@app.post("/chamados", status_code=201)
def criar_chamado(chamado: Chamado):
    novo_chamado = {
        "id": len(chamados) + 1,
        **chamado.model_dump()
    }

    chamados.append(novo_chamado)

    return novo_chamado


@app.get("/chamados/{id}")
def buscar_chamado(id: int):
    for chamado in chamados:
        if chamado["id"] == id:
            return chamado

    raise HTTPException(
        status_code=404,
        detail="Chamado não encontrado."
    )


@app.get("/chamados/status/{status_chamado}")
def listar_por_status(status_chamado: str):
    resultado = [
        chamado
        for chamado in chamados
        if chamado["status"].lower() == status_chamado.lower()
    ]

    return resultado