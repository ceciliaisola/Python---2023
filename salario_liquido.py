# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. 
# quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. 
# calcule os descontos e o salário líquido,

salario_hora = float(input("Digite quanto você ganha por hora: R$"))
n_horas = float(input("Digite quantas horas você trabalha no mês: "))

salario_bruto = salario_hora * n_horas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print(
    f" + Salário Bruto : R${salario_bruto}\n"
    f" - IR (11%) : R${ir}\n"
    f" - INSS (8%) : R${inss}\n"
    f" - Sindicato (5%) : R${sindicato}\n"
    f" = Salário Líquido : R${salario_liquido}")