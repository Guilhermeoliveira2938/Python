num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
operacao = input('Escolha uma operação: (- + * / ** rm): ')
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
elif operacao == 'r':
    print('O resultado das raizes é: ', num1 ** (1/2), num2 ** (1/2))