dia = int(input("Por quantos dias o carro foi alugado? "))
valor_dia = dia * 60
Km = float(input("Quantos Kms foram rodados?"))
valor_km = Km * 0.15
valor_final = valor_dia + valor_km
print("O valor a ser pago pelo carro é de ${}".format(valor_final))