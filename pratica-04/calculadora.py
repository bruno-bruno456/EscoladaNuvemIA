while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, * ou /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            raise ValueError("Operação Inválida")    

        print(f"O resultado é: {resultado}")            
        break

    except ZeroDivisionError:
        print(f"Erro: divisão por zero não é permitida. Por favor, tente novamente.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, tente novamente.")    