from joint_probability import joint_probabilty

def inferencia_marginal(query: dict, evidencia: dict) -> float:
    total = 0.0

    for b in [0, 1]:
        for e in [0, 1]:
            for a in [0, 1]:

                assignment = {'b': b, 'e': e, 'a': a}

                if any(assignment[var] != val for var, val in evidencia.items()):
                    continue

                if all(assignment[var] == val for var, val in query.items()):
                    total += joint_probabilty(b, e, a)

    return total