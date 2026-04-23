from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/automata", tags=["automata"])

# Aquí agregaremos las rutas para los 3 ejercicios

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "API funcionando correctamente."}
