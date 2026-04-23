from pydantic import BaseModel
from typing import List

class EvaluationRequest(BaseModel):
    cadena: str

class StepInfo(BaseModel):
    simbolo: str
    estados_activos: List[str]

class EvaluationResponse(BaseModel):
    aceptada: bool
    recorrido: List[StepInfo]
    mensaje: str
