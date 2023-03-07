print("Insira 3 números (n1,n2,n3) para verificar qual o maior deles!")

n1 = int(input("n1= "))
n2 = int(input("n2= "))
n3 = int(input("n3= "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número")
else:
    print(f"{n3} é o maior número")