# Função principal
def calculadora():
    # Recebe o primeiro número do usuário
    numero1 = float(input("Digite o primeiro número: "))
    
    # Recebe o segundo número do usuário
    numero2 = float(input("Digite o segundo número: "))
    
    # Recebe o tipo de operação do usuário
    operacao = input("Digite o tipo de operação (+, -, *, /): ")
    
    # Verifica o tipo de operação e executa a operação correspondente
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operação inválida."
    
    # Retorna o resultado da operação
    return resultado

# Chama a função e imprime o resultado
resultado = calculadora()
print("Resultado:", resultado)
