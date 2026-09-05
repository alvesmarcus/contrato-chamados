from sqlalchemy.orm import Session

from models import Chamado
from schemas import ChamadoCreate


def criar_chamado(db: Session, chamado: ChamadoCreate):
    novo_chamado = Chamado(
        titulo=chamado.titulo,
        descricao=chamado.descricao,
        status=chamado.status
    )

    db.add(novo_chamado)
    db.commit()
    db.refresh(novo_chamado)

    return novo_chamado


def listar_chamados(db: Session):
    return db.query(Chamado).all()


def buscar_chamado(db: Session, chamado_id: int):
    return db.query(Chamado).filter(Chamado.id == chamado_id).first()