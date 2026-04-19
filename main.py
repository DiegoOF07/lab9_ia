from joint_probability import joint_probabilty, p_a_given_be
from inference import inferencia_marginal
from explain_away import diagnostico_simple, explain_away

def main():
    print(f"{'B':>2} {'E':>2} {'A':>2}  {'P(A|B,E)':>10}  {'P(B,E,A)':>14}")
    total = 0
    for b in [0, 1]:
        for e in [0, 1]:
            for a in [0, 1]:
                p = joint_probabilty(b, e, a)
                pa = p_a_given_be(a, b, e)
                total += p
                print(f"{b:>2} {e:>2} {a:>2}  {pa:>10.1f}  {p:>14.10f}")

    print(f"{'Suma total:':>18}  {total:>14.10f}")
    
    # Task 2.2: Mostrando la probabilidad marginal de A=1
    p_a = inferencia_marginal(query={'a': 1}, evidencia={})
    print(f"P(A=1) = {p_a:.6f}")
    pass

    # Task 2.3: Explain Away

    '''
        Al observar únicamente la alrma, la probabilidad de robo es alta debido a la 
        incertidumbre entre múltiples causas posibles. No obstante, al incorporar 
        evidencia adicional (terremoto), la probabilidad de robo disminuye significativamente, 
        ya que la nueva evidencia explica activación de la alarma. 
    '''

    print("\nExplain Away")
    p1 = diagnostico_simple()
    p2 = explain_away()

    print(f"P(B=1 | A=1) = {p1:.4f}")
    print(f"P(B=1 | A=1, E=1) = {p2:.4f}")


if __name__ == "__main__":
    main()
