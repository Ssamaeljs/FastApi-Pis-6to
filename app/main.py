from fastapi import FastAPI
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from models.persona import Persona
import datetime
app = FastAPI()

@app.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse(url="/docs")

@app.post("/registrarse")
def registrarse(persona: Persona):
    return {"msg": "Registrado exitosamente", "code": 200, "persona": persona}

@app.post("/iniciar_sesion")
def iniciar_sesion(correo: str, clave: str):
    if correo != "user.example@unl.edu.ec" or clave != "12345678":
        return {"msg": "Credenciales incorrectas", "code": 200}
    return {"msg": "Bienvenido Usuario", 
            "code": 200, 
            "user": {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
                "nombre": "User",
                "apellido": "Example",
                "external_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
                "cuenta": {
                    "correo": correo,
                    "rol": "USUARIO",
                    "descripcion": "Usuario de prueba",
                    "descripcion_pdf": "a157b0da-a14d-4584-8fe7-a43a762a14d0.pdf",
                    "estado": "EN ESPERA",
                    "external_id": "d290f1ee-6c54-4b01-90e6-d701748f0851"
                    }
                }
            }

@app.get("/listar/dispositivo")
def listar_dispositivos():
    return {"msg": "Listado de dispositivos", 
            "code": 200, 
            "info": [
                {
                    "nombre": "Dispositivo 1",
                    "descripcion": "Dispositivo de prueba 1",
                    "external_id": "d290f1ee-6c54-4b01-90e6-d701748f0851"
                    
                    },
                {
                    "nombre": "Dispositivo 2",
                    "descripcion": "Dispositivo de prueba 2",
                    "external_id": "d290f1ee-6c54-4b01-90e6-d701748f0852"
                    },
                {
                    "nombre": "Dispositivo 3",
                    "descripcion": "Dispositivo de prueba 3",
                    "external_id": "d290f1ee-6c54-4b01-90e6-d701748f0853"
                    }
                ]
            }
        
    
