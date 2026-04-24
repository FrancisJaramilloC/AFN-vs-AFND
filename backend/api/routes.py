from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.schemas import EvaluationRequest

from backend.core.afd.validador_bancario import validador_bancario_afd
from backend.core.afd.sistema_seguridad import sistema_seguridad_afd
from backend.core.afd.notacion_cientifica import notacion_cientifica_afd, preprocesar_notacion

router = APIRouter(prefix="/api/automata", tags=["automata"])

@router.post("/ejercicio1/evaluar")
def evaluar_ejercicio1(req: EvaluationRequest):
    res_afd = validador_bancario_afd.evaluar(req.cadena)
    return {"afd": res_afd}


@router.post("/ejercicio2/evaluar")
def evaluar_ejercicio2(req: EvaluationRequest):
    res_afd = sistema_seguridad_afd.evaluar(req.cadena)
    return {"afd": res_afd}


@router.post("/ejercicio3/evaluar")
def evaluar_ejercicio3(req: EvaluationRequest):
    cadena_original = req.cadena
    cadena_procesada = preprocesar_notacion(cadena_original)
    res_afd = notacion_cientifica_afd.evaluar(cadena_procesada)
    # Incluimos la cadena procesada para que el usuario vea la traducción
    res_afd["cadena_original"] = cadena_original
    res_afd["cadena_procesada"] = cadena_procesada
    return {"afd": res_afd}


@router.get("/health")
def health_check():
    return {"status": "ok", "message": "API funcionando correctamente."}
