import pandas as pd 
import matplotlib.pyplot as plt
# abrir o terminal ctrl + ' 
# pip install pandas e pip install matplotlib
# idades = [17, 16, 16, 16, 17, 16, 16, 16, 16, 16, 17, 16, 18, 16, 16, 16, 16, 16, 16]
idades = []
print("Digite as idades (digite sair para finalizar)")
while True:
    entrada = input("Idade: ")
    if entrada.lower() == "sair":
        break
    try: 
        idade = int(entrada)
        if idade < 0: 
            print("Idade não pode ser negativa!")
            continue
        idades.append(idade)
    except ValueError:
        print("Somente números válidos (só inteiros)")
if len(idades) == 0:
    print("Nenhuma idade válida foi inserida!")
    exit()       
# Criando uma visualização de dados
df = pd.DataFrame(idades, columns=["Idade"])
bins = [0, 12, 17, 25, 40, 60, 100]
labels = ["Criança", "Adolescente", "Jovem", "Adulto", "Meia-idade", "Idoso"]
df["Faixa Etária"] = pd.cut(df["Idade"], bins=bins, labels = labels)
print("\nEstatísticas: ")
print(f"Média: {df['Idade'].mean():.2f}")
print(f"Mediana: {df['Idade'].median()}")
df["Faixa Etária"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribuição por faixa etária")
plt.xlabel("Faixa Etária")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()