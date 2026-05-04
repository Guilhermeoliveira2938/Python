sal = float(input("Digite o seu salário atual: "))
porcent = 15
aum = (sal * porcent) / 100
novo_sal = sal + aum
print("Seu novo salario é de {:.2f} reais".format(novo_sal))