sal_bruto = int(input("Digite o salario que você quer verificar: "))
porcent_dia = int(input("Digite a porcentagem a ser cobrada do dia: "))
if porcent_dia == 50:
    val_hora = sal_bruto / 220
    #porcentagem = 50
    #val_extra = (val_hora + porcentagem) / 100
    val_extra = val_hora * 1.5
    horas = int(input("Digite as horas: "))
    pagar = val_extra * horas
    print(val_hora)
    print(val_extra)
    print("O valor a ser pago de horas extras são de: {}".format(pagar))
else:
    val_hora = sal_bruto / 220
    # porcentagem = 50
    # val_extra = (val_hora + porcentagem) / 100
    val_extra = val_hora * 2
    horas = int(input("Digite as horas: "))
    pagar = val_extra * horas
    print(val_hora)
    print(val_extra)
    print("O valor a ser pago de horas extras são de: {}".format(pagar))


