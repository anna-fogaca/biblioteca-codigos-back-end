# EX 06

numeroA = float(input("Digite o 1º número: "))
numeroB = float(input("Digite o 2º número: "))
numeroC = float(input("Digite o 3º número: "))

if numeroA > numeroB and numeroA > numeroC:
    print(f"Número 1: {numeroA} é maior!")
elif numeroB > numeroA and numeroB > numeroC:
    print(f"Número 2: {numeroB} é maior!")
else: 
    print(f"Número 3: {numeroC} é maior!")