# EX 07
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f"Você foi aprovado! Sua média é: {media:.1f}")
else: 
    print(f"Você foi reprovado! Sua média é: {media:.1f}")
    
    