from backend.core.automata import AutomataEngine

# Ejercicio 6: Reconocimiento Genético (AFND)
# Alfabeto: k (Lys), g (Gly), f (Phe), x (Cualquiera)
# Patrón: k g x* f

transiciones = {
    'q0': {'k': ['q1']},
    'q1': {'g': ['q2']},
    'q2': {
        'k': ['q2'],
        'g': ['q2'],
        'x': ['q2'],
        'f': ['q2', 'q3']  # No determinismo puro
    },
    'q3': {}
}

secuencia_genetica_afnd = AutomataEngine(
    tipo="AFND",
    estados={'q0', 'q1', 'q2', 'q3'},
    alfabeto={'k', 'g', 'f', 'x'},
    transiciones=transiciones,
    q0='q0',
    finales={'q3'}
)
