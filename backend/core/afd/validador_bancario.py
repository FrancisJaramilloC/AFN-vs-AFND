from backend.core.automata import AutomataEngine

# Ejercicio 1: Validador de Flujo de Transacciones Bancarias (AFD)
# Alfabeto: 'a' (Autorizar), 'c' (Capturar), 'l' (Liquidar)

transiciones = {
    'q0': {'a': ['q1'], 'c': ['qE'], 'l': ['qE']},
    'q1': {'a': ['qE'], 'c': ['q2'], 'l': ['qE']},
    'q2': {'a': ['qE'], 'c': ['qE'], 'l': ['q3']},
    'q3': {'a': ['qE'], 'c': ['qE'], 'l': ['qE']},
    'qE': {'a': ['qE'], 'c': ['qE'], 'l': ['qE']}
}

validador_bancario_afd = AutomataEngine(
    tipo="AFD",
    estados={'q0', 'q1', 'q2', 'q3', 'qE'},
    alfabeto={'a', 'c', 'l'},
    transiciones=transiciones,
    q0='q0',
    finales={'q3'}
)
