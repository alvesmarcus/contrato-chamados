from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from typing import Literal


class ChamadoCreate(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=120)
    descricao: str = Field(..., min_length=1)
    status: Literal["aberto", "em_andamento", "fechado"] = "aberto"


class ChamadoResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    status: str
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)