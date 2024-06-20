# Função principal
def verificar_palindromo():
    # Recebe uma palavra do usuário
    palavra = input("Digite uma palavra: ")
    
    # Converte a palavra para minúsculas para tornar a verificação insensível a maiúsculas/minúsculas
    palavra = palavra.lower()
    
    # Verifica se a palavra é igual ao seu reverso
    if palavra == palavra[::-1]:
        resultado = "A palavra '{}' é um palíndromo.".format(palavra)
    else:
        resultado = "A palavra '{}' não é um palíndromo.".format(palavra)
    
    # Retorna ou exibe o resultado
    return resultado

# Chama a função e imprime o resultado
resultado = verificar_palindromo()
print(resultado)
