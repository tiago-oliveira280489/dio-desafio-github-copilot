# Função principal
def calcular_media():
    # Recebe as três notas do usuário
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # Calcula a média aritmética
    media = (nota1 + nota2 + nota3) / 3
    
    # Retorna ou exibe a média
    return media

# Chama a função e imprime o resultado
resultado = calcular_media()
print("A média aritmética das notas informadas é:", resultado)
