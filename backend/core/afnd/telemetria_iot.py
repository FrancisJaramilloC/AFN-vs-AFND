from backend.core.automata import AutomataEngine

# Ejercicio 5: Validación de Protocolo IoT (AFND)
# Alfabeto: h (HDR), t (TEMP), m (HUM), c (CRC)
# Lenguaje: h (t|m)* c

transiciones = {
    'q0': {'h': ['q1']},
    'q1': {
        't': ['q1'], 
        'm': ['q1'], 
        'c': ['q2']
    },
    'q2': {}
}

telemetria_iot_afnd = AutomataEngine(
    tipo="AFND",
    estados={'q0', 'q1', 'q2'},
    alfabeto={'h', 't', 'm', 'c'},
    transiciones=transiciones,
    q0='q0',
    finales={'q2'}
)
