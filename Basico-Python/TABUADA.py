# TABUADA
numero = int(input("Digite a tabuada escolhida - De 1 ao 10: "))
print(f"A tabuada escolhida foi: {numero}")
i = 1
for i in range(11):
    print(f"{numero} X {i}: {numero * i}")
    i = i + 1