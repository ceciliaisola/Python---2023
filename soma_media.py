# Faça um programa que leia 5 números e informe a soma e a média dos números

lista = []
soma = 0

for i in range (1,6):
    numero = int(input("Número" + str([i]) + ": "))
    lista.append(numero)
    soma = soma + numero

print(f"A soma desses números é {soma}.")
print(f"A média desses números é {soma/5}.")