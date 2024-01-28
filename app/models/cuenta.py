from typing import Optional
from enum import Enum
from pydantic import BaseModel
from uuid import uuid4
class RolEnum(str, Enum):
    ADMINISTRADOR = "ADMINISTRADOR"
    USUARIO = "USUARIO"

class EstadoEnum(str, Enum):
    EN_ESPERA = "EN ESPERA"
    RECHAZADO = "RECHAZADO"

class Cuenta(BaseModel):
    correo: str
    clave: str
    description: Optional[str] = None
    description_pdf: Optional[str] = None
    rol: RolEnum
    estado: EstadoEnum
    external_id: Optional[str] = uuid4()