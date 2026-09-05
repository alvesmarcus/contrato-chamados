from sqlalchemy import Column, Integer, String, Text, DateTime, CheckConstraint
from sqlalchemy.sql import func

from database import Base


class Chamado(Base):
    __tablename__ = "chamados"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(120), nullable=False)
    descricao = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, default="aberto")
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (
        CheckConstraint(
            "status IN ('aberto', 'em_andamento', 'fechado')",
            name="chamados_status_valido"
        ),
    )