#
#
#
# 8. (OBI 2014) Escreva um programa que receba 
# um número inteiro N 
# como entrada e exiba a quantidade de 
# dígitos desse número.

n = int(input("Digite um número inteiro: ")) # entrada de dados (número inteiro) 
quantidade_digitos = len(str(n)) # processamento (conversão para string e contagem de caracteres)
print(f"Quantidade de dígitos: {quantidade_digitos}") # saída de dados (quantidade de dígitos)
