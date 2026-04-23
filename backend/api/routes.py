from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.schemas import EvaluationRequest

from backend.core.afd.validador_bancario import validador_bancario_afd
from backend.core.afd.sistema_seguridad import sistema_seguridad_afd

router = APIRouter(prefix="/api/automata", tags=["automata"])

@router.post("/ejercicio1/evaluar")
def evaluar_ejercicio1(req: EvaluationRequest):
    res_afd = validador_bancario_afd.evaluar(req.cadena)
    return {"afd": res_afd}


@router.post("/ejercicio2/evaluar")
def evaluar_ejercicio2(req: EvaluationRequest):
    res_afd = sistema_seguridad_afd.evaluar(req.cadena)
    return {"afd": res_afd}

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "API funcionando correctamente."}
