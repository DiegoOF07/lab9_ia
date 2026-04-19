from joint_probability import joint_probabilty, p_a_given_be
from inference import inferencia_marginal

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

if __name__ == "__main__":
    main()
