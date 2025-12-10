# QUESTÃO 1 - Cadastro de Aviões

avioes = [None] * 4

print("=== Cadastro dos Aviões ===")
for i in range(4):
    avioes[i] = input(f"Digite o número do avião {i+1}: ")

print("\nAviões cadastrados:")
for a in avioes:
    print("-", a)

# QUESTÃO 2 - Cadastro de Assentos

avioes = [input(f"Informe o número do avião {i+1}: ") for i in range(4)]
assentos_totais = [0] * 4
assentos_disponiveis = [0] * 4

print("\n=== Cadastro de Assentos ===")
for i in range(4):
    total = int(input(f"Assentos totais do avião {avioes[i]}: "))
    assentos_totais[i] = total
    assentos_disponiveis[i] = total

print("\nCadastro concluído!")

# QUESTÃO 3 - Fazer Reserva Completa

class Reserva:
    def __init__(self, codigo, aviao, nome, assento, classe, origem, destino):
        self.codigo = codigo
        self.aviao = aviao
        self.nome = nome
        self.assento = assento
        self.classe = classe
        self.origem = origem
        self.destino = destino


avioes = ["101", "202", "303", "404"]
assentos_totais = [20, 15, 10, 30]
assentos_disponiveis = [20, 15, 10, 30]
reservas = []
contador = 1

def encontrar(aviao):
    return avioes.index(aviao) if aviao in avioes else -1

print("=== Fazer Reserva ===")

if len(reservas) >= 10:
    print("Limite máximo de reservas atingido!")
else:
    av = input("Número do avião: ")
    idx = encontrar(av)

    if idx == -1:
        print("Avião não encontrado.")
    elif assentos_disponiveis[idx] == 0:
        print("Sem assentos disponíveis.")
    else:
        nome = input("Nome passageiro: ")
        origem = input("Origem: ")
        destino = input("Destino: ")
        classe = input("Classe do assento: ")
        assento = input("Número do assento: ")

        codigo = f"SF-{contador:03d}"
        contador += 1

        reservas.append(Reserva(codigo, av, nome, assento, classe, origem, destino))
        assentos_disponiveis[idx] -= 1

        print("\nReserva concluída com sucesso!")
        print("Código:", codigo)

        # QUESTÃO 4 - Consulta por Avião

class Reserva:
    def __init__(self, codigo, aviao, nome, assento, classe, origem, destino):
        self.codigo = codigo
        self.aviao = aviao
        self.nome = nome
        self.assento = assento
        self.classe = classe
        self.origem = origem
        self.destino = destino

reservas = [
    Reserva("SF-001", "101", "Ana", "12A", "Econômica", "SP", "RJ"),
    Reserva("SF-002", "101", "Carlos", "14B", "Econômica", "SP", "BH"),
]

print("=== Consulta por Avião ===")
numero = input("Número do avião: ")

lista = [r for r in reservas if r.aviao == numero]

if len(lista) == 0:
    print("Nenhuma reserva para este avião.")
else:
    print(f"\nReservas do avião {numero}:")
    for r in lista:
        print(f"- {r.nome} | Assento {r.assento} | {r.origem} → {r.destino}")


# QUESTÃO 5 - Consulta por Passageiro

class Reserva:
    def __init__(self, codigo, aviao, nome, assento, classe, origem, destino):
        self.codigo = codigo
        self.aviao = aviao
        self.nome = nome
        self.assento = assento
        self.classe = classe
        self.origem = origem
        self.destino = destino

reservas = [
    Reserva("SF-001", "101", "Ana", "12A", "Econômica", "SP", "RJ"),
    Reserva("SF-002", "202", "Ana", "3C", "Executiva", "RJ", "BA"),
]

print("=== Consulta por Passageiro ===")
nome = input("Nome: ")

lista = [r for r in reservas if r.nome.lower() == nome.lower()]

if len(lista) == 0:
    print("Nenhuma reserva encontrada.")
else:
    print(f"\nReservas de {nome}:")
    for r in lista:
        print(f"- Código {r.codigo} | Avião {r.aviao} | Assento {r.assento}")

# QUESTÃO 6 - Relatórios + Gráficos

import matplotlib.pyplot as plt

avioes = ["101", "202", "303", "404"]
reservas = [7, 1, 9, 3]
assentos_totais = [20, 15, 10, 30]
assentos_disponiveis = [20-7, 15-1, 10-9, 30-3]

# Gráfico de Barras
plt.figure(figsize=(8,5))
plt.bar(avioes, reservas, color='royalblue')
plt.title("Reservas por Avião")
plt.xlabel("Avião")
plt.ylabel("Reservas")
plt.show()

# Gráfico de Pizza
ocupacao = [r/t*100 for r,t in zip(reservas, assentos_totais)]
plt.figure(figsize=(7,7))
plt.pie(ocupacao, labels=avioes, autopct="%1.1f%%", startangle=90)
plt.title("Ocupação (%) por Avião")
plt.show()

# Gráfico de Linha
plt.figure(figsize=(8,5))
plt.plot(avioes, assentos_disponiveis, marker='o', color='green')
plt.title("Assentos Disponíveis por Avião")
plt.xlabel("Avião")
plt.ylabel("Assentos Disponíveis")
plt.grid(True)
plt.show()
