from typing import Optional
from pydantic import BaseModel
import datetime
from models import cuenta
from uuid import uuid4
class Persona(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: datetime.date
    cargo: str
    institucion: str
    external_id: Optional[str] = uuid4()
    cuenta: cuenta.Cuenta
    
