from inference import inferencia_marginal

def probabilidad_condicional(query: dict, evidencia: dict) -> float:
    # P(query ∧ evidencia)
    numerador = inferencia_marginal(query={**query, **evidencia},evidencia={})

    # P(evidencia)
    denominador = inferencia_marginal(query=evidencia,evidencia={})

    if denominador == 0:
        return 0.0

    return numerador / denominador


def diagnostico_simple() -> float:
    # P(B=1 | A=1)
    return probabilidad_condicional(query={'b': 1},evidencia={'a': 1})


def explain_away() -> float:
    # P(B=1 | A=1, E=1)
    return probabilidad_condicional(query={'b': 1},evidencia={'a': 1, 'e': 1})