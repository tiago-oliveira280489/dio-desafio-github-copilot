# Função principal
def verificar_par_ou_impar():
    # Recebe um número inteiro do usuário
    numero = int(input("Digite um número inteiro: "))
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        resultado = "O número {} é par.".format(numero)
    else:
        resultado = "O número {} é ímpar.".format(numero)
    
    # Retorna ou exibe o resultado
    return resultado

# Chama a função e imprime o resultado
resultado = verificar_par_ou_impar()
print(resultado)
