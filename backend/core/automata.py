# Módulo central para la simulación de AFD y AFND.
from typing import List, Dict, Set

class AutomataEngine:
    def __init__(self, tipo: str, estados: Set[str], alfabeto: Set[str], transiciones: Dict[str, Dict[str, List[str]]], q0: str, finales: Set[str]):
        self.tipo = tipo
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones # Formato: {'q0': {'a': ['q1', 'q2'], ...}, ...}
        self.q0 = q0
        self.finales = finales

    def evaluar(self, cadena: str):
        # Mantiene los estados activos en un conjunto (set)
        estados_activos = {self.q0}
        recorrido = [{"simbolo": "Inicial", "estados_activos": list(estados_activos)}]
        
        for simbolo in cadena:
            nuevos_estados = set()
            if simbolo not in self.alfabeto:
                # Símbolo no reconocido, en AFD suele ir a error, en AFND muere la rama
                pass
            else:
                for estado in estados_activos:
                    if estado in self.transiciones and simbolo in self.transiciones[estado]:
                        # Agrega todos los destinos posibles (múltiples en AFND, uno en AFD)
                        for dest in self.transiciones[estado][simbolo]:
                            nuevos_estados.add(dest)
            
            estados_activos = nuevos_estados
            recorrido.append({"simbolo": simbolo, "estados_activos": list(estados_activos)})
            
            # Optimización: Si no hay estados activos (se murieron todas las ramas), rechaza de inmediato
            if not estados_activos:
                break
                
        aceptada = any(estado in self.finales for estado in estados_activos)
        
        return {
            "aceptada": aceptada,
            "recorrido": recorrido,
            "mensaje": "Cadena aceptada." if aceptada else "Cadena rechazada."
        }


