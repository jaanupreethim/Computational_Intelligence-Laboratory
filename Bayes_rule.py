P_E_given_H = []
P_H = []

n = int(input("Enter no. of hypothesis: "))

for i in range(n):
    ph = float(input(f"Enter probability P(H{i+1}): "))
    peh = float(input(f"Enter probability P(E|H{i+1}): "))
    P_H.append(ph)
    P_E_given_H.append(peh)

P_E = 0
for i in range(n):
    P_E += P_E_given_H[i] * P_H[i]

print("\n--- Posterior Probabilities ---")
if P_E == 0:
    print("Total evidence P(E) is 0; cannot divide by zero.")
else:
    for i in range(n):
        P_H_given_E = (P_E_given_H[i] * P_H[i]) / P_E
        print(f"P(H{i+1}|E) = {P_H_given_E:.4f}")
