

# Primeira API de Chamados com FastAPI

# Integrantes:
# - Andrew Lippy de Mattos Pereira
# - Cauã Pereira Menezes
# - Marcus Vinicius Alves de Oliveira
# - Matheus Prates Gaspar Silva
# - Nathan de Faria Alves Alvarenga
# - Roberto Kleber da Fonseca Ponce Junior



## Sobre o projeto

Este projeto foi desenvolvido como parte de uma atividade prática da disciplina, com o objetivo de aprender os primeiros conceitos de criação de APIs utilizando Python e FastAPI.

A API simula um sistema simples de chamados, permitindo cadastrar, consultar e filtrar chamados. Nesta primeira versão, os dados ficam armazenados em uma lista na memória, sem utilização de banco de dados.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic

## O que a API faz

A aplicação possui as seguintes funcionalidades:

- Verificar se a API está funcionando;
- Listar os chamados cadastrados;
- Criar novos chamados;
- Consultar um chamado pelo seu ID;
- Informar quando um chamado não foi encontrado;
- Validar os dados enviados;
- Filtrar chamados pelo status.

## Como executar

Primeiro, é necessário criar e ativar o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1