num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
operacao = input('Escolha uma operação: (- + * / **): ')
if operacao == '+':
    print("O resultado é: ", num1 + num2)
elif operacao == '-':
    print("O resultado é: ",num1 - num2)
elif operacao == '*':
    print("O resultado é: ", num1 * num2)
elif operacao == '/':
    print("O resultado é: ", num1 / num2)
elif operacao == '**':
    print("O resultado é: ", num1 ** num2)
