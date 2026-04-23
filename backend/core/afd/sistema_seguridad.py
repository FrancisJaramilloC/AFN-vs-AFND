from backend.core.automata import AutomataEngine

# Ejercicio 2: Sistema de Seguridad IoT - Cerradura Inteligente (AFD)
# Alfabeto: 'c' (Correcto), 'i' (Incorrecto)
# Basado en el diagrama de JFLAP: 
# q0 es el único estado de aceptación. Tras 3 errores se llega a q3, y cualquier otra entrada lleva a qBloq.

transiciones = {
    'q0': {'c': ['q0'], 'i': ['q1']},
    'q1': {'c': ['q0'], 'i': ['q2']},
    'q2': {'c': ['q0'], 'i': ['q3']},
    'q3': {'c': ['qBloq'], 'i': ['qBloq']},
    'qBloq': {'c': ['qBloq'], 'i': ['qBloq']}
}

sistema_seguridad_afd = AutomataEngine(
    tipo="AFD",
    estados={'q0', 'q1', 'q2', 'q3', 'qBloq'},
    alfabeto={'c', 'i'},
    transiciones=transiciones,
    q0='q0',
    finales={'q0'}
)
