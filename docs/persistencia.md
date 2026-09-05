
# Tarefa 2 — Persistência de Chamados de Suporte

Integrantes:
- Andrew Lippy de Mattos Pereira
- Cauã Pereira Menezes
- Marcus Vinicius Alves de Oliveira
- Matheus Prates Gaspar Silva
- Nathan de Faria Alves Alvarenga
- Roberto Kleber da Fonseca Ponce Junior


## 1. Objetivo

Nesta tarefa, nosso objetivo foi integrar a API de chamados com um banco de dados PostgreSQL.

Na tarefa anterior, trabalhamos apenas com o planejamento do sistema. Nesta etapa, começamos a implementação do back-end e criamos uma estrutura para que os chamados sejam armazenados no banco de dados e não sejam perdidos quando a aplicação for encerrada.

Para o desenvolvimento, utilizamos Python, FastAPI, SQLAlchemy e PostgreSQL.

---

## 2. Modelo do Chamado

Para representar um chamado, utilizamos os seguintes campos:

- **id:** identificador único do chamado;
- **titulo:** título do chamado, sendo obrigatório;
- **descricao:** descrição do problema, sendo obrigatória;
- **status:** situação atual do chamado;
- **criado_em:** data e hora em que o chamado foi criado.

Os status definidos para os chamados são:

- `aberto`
- `em_andamento`
- `fechado`

A representação do modelo ficou:

```text
Chamado
- id: identificador único
- titulo: texto obrigatório
- descricao: texto obrigatório
- status: aberto | em_andamento | fechado
- criado_em: data e hora de criação