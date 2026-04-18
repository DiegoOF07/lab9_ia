EPS = 0.01

def p_of_b(b: int) -> float:
    return EPS if b == 1 else 1 - EPS

def p_of_e(e: int) -> float:
    return EPS if e == 1 else 1 - EPS

def p_a_given_be(a: int, b: int, e: int) -> float:
    alarm_on = int(b == 1 or e == 1)
    return 1.0 if a == alarm_on else 0.0

def joint_probabilty(b: int, e: int, a: int) -> float:
    return p_of_b(b) * p_of_e(e) * p_a_given_be(a, b, e)

