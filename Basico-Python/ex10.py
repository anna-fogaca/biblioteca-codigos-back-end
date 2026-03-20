while(True):
    numero = int(input("Digite um número: "))
    for i in range(numero):
        soma = numero + soma
        if numero == 0:
            print("O sistema parou!")
            print(f"A soma de todos os números é: {soma}")
            break
    