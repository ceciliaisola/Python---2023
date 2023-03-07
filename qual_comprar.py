# Faça um programa que pergunte o preço de três produtos e informe 
# qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print("Informe o preço de 3 produtos e informaremos qual você deve comprar!")

p1 = float(input("Preço do produto 1: "))
p2 = float(input("Preço do produto 2: "))
p3 = float(input("Preço do produto 3: "))

if p1 < p2 and p1 < p3:
    print("Você deve comprar o produto 1!")
elif p2 < p1 and p2 < p3:
    print("Você deve comprar o produto 2!")
else:
    print("Você deve comprar o produto 3!")