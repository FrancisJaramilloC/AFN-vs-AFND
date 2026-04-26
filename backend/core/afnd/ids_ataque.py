from backend.core.automata import AutomataEngine

# Ejercicio 4: Detección de Patrones de Ataque IDS (AFND)
# Alfabeto: 's' (SYN), 'a' (ACK), 'r' (RST)
# Lenguaje: s a+ r
# Demuestra no-determinismo en q1 permitiendo múltiples caminos con 'a'.

transiciones = {
    'q0': {'s': ['q1']},
    'q1': {'a': ['q1', 'q2']}, # No determinismo: puede quedarse en q1 o pasar a q2
    'q2': {'r': ['q3']},
    'q3': {}
}

ids_ataque_afnd = AutomataEngine(
    tipo="AFND",
    estados={'q0', 'q1', 'q2', 'q3'},
    alfabeto={'s', 'a', 'r'},
    transiciones=transiciones,
    q0='q0',
    finales={'q3'}
)
