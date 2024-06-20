# Função principal
def repetir_string():
    # Recebe a string do usuário
    string = input("Digite uma string: ")
    
    # Recebe o número inteiro do usuário
    numero = int(input("Digite um número inteiro: "))
    
    # Repete a string o número de vezes informado
    string_repetida = (string + '\n') * numero
    
    # Retorna ou exibe a string repetida
    return string_repetida

# Chama a função e imprime o resultado
resultado = repetir_string()
print("String repetida:", resultado)
