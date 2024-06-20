# Função principal
def concatena_dados():
    # Recebe o primeiro dado do usuário
    dado1 = input("Digite o primeiro dado: ")
    
    # Recebe o segundo dado do usuário
    dado2 = input("Digite o segundo dado: ")
    
    # Concatena os dois dados em uma única string
    dados_concatenados = dado1 + " " + dado2
    
    # Retorna ou exibe a string concatenada
    return dados_concatenados

# Chama a função e imprime o resultado
resultado = concatena_dados()
print("Dados concatenados:", resultado)
