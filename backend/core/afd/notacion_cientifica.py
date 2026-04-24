from backend.core.automata import AutomataEngine

# Ejercicio 3: Analizador Léxico para Notación Científica (AFD)
# Alfabeto abstracto: 's' (signo +/-), 'd' (dígito 0-9), 'p' (punto .), 'e' (exponente e/E)
#
# Basado en el diagrama JFLAP del equipo:
#   q0     -> Inicio
#   q1     -> Después de signo (+/-)
#   q2     -> Después de dígito(s) en parte entera (ACEPTACIÓN)
#   q3     -> Después de punto decimal (esperando decimales)
#   q4     -> Después de dígito(s) en parte decimal (ACEPTACIÓN)
#   q5     -> Después de 'e'/'E' (marcador de exponente)
#   q6     -> Después de signo en exponente
#   q7     -> Después de dígito(s) en exponente (ACEPTACIÓN)
#   qError -> Estado trampa / error

transiciones = {
    'q0':     {'s': ['q1'], 'd': ['q2'], 'p': ['q3'], 'e': ['qError']},
    'q1':     {'s': ['qError'], 'd': ['q2'], 'p': ['q3'], 'e': ['qError']},
    'q2':     {'s': ['qError'], 'd': ['q2'], 'p': ['q3'], 'e': ['q5']},
    'q3':     {'s': ['qError'], 'd': ['q4'], 'p': ['qError'], 'e': ['qError']},
    'q4':     {'s': ['qError'], 'd': ['q4'], 'p': ['qError'], 'e': ['q5']},
    'q5':     {'s': ['q6'], 'd': ['q7'], 'p': ['qError'], 'e': ['qError']},
    'q6':     {'s': ['qError'], 'd': ['q7'], 'p': ['qError'], 'e': ['qError']},
    'q7':     {'s': ['qError'], 'd': ['q7'], 'p': ['qError'], 'e': ['qError']},
    'qError': {'s': ['qError'], 'd': ['qError'], 'p': ['qError'], 'e': ['qError']}
}

notacion_cientifica_afd = AutomataEngine(
    tipo="AFD",
    estados={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qError'},
    alfabeto={'s', 'd', 'p', 'e'},
    transiciones=transiciones,
    q0='q0',
    finales={'q2', 'q4', 'q7'}
)


def preprocesar_notacion(cadena_real: str) -> str:
    """
    Convierte una cadena real de notación científica al alfabeto del autómata.
    Ej: "+3.14e-10" -> "sdpddesdd"
    """
    resultado = []
    for char in cadena_real:
        if char in ('+', '-'):
            resultado.append('s')
        elif char.isdigit():
            resultado.append('d')
        elif char == '.':
            resultado.append('p')
        elif char.lower() == 'e':
            resultado.append('e')
        else:
            resultado.append('?')  # Carácter inválido
    return ''.join(resultado)
