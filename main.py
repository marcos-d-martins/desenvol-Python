num1 = float(input("digite o primeiro valor:"))
num2 = float(input("digite o segunda valor:"))
operacao = (input("escolha a operação: (+, -, *, /)"))

#REALIZANDO As OPERAÇÕES
if operacao == "+":
    resultado = num1 + num2
    print(f"o resultado da soma é:{resultado}")
elif operacao == "-":
    if num1 > num2:
        resultado = num1 - num2
        print(f"o resultado da subtração é:{resultado}")
    else:
        resultado = num2 - num1
        print(f"o resultado da subtração é:{resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"o resultado da multiplicação é:{resultado}")
elif operacao == "/":
    if num2 != 0:

        if num1 > num2:
            resultado = num1 / num2
            print(f"o resultado da divisão é:{resultado}")
        else:
            resultado = num2 / num1
            print(f"o resultado da divisão é:{resultado}")
else:
    print("operação inválida. Por favor escolha entre +, -, *, /")
    