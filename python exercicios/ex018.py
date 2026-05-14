from math import hypot
cat_opo = float(input("Digite o cateto oposto do seu triângulo: "))
cat_adj = float(input("Digite o cateto adjacente do seu triângulo: "))
hipotenusa = hypot(cat_opo,cat_adj)
print("A hipotenusa do seu triângulo é: {:.2f}".format(hipotenusa))