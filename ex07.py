#
#
#
# 7. (OBI 2015) Escreva um programa que leia uma sequência de números 
# inteiros e exiba a média aritmética dos números digitados.

numeros = input("Digite uma sequência de números separados por espaço: ").split() # separa a string em uma lista de strings
numeros = list(map(int, numeros)) # converte a lista de strings para inteiros
media = sum(numeros) / len(numeros) # calcula a média aritmética dos números da lista 
print(f"A média aritmética é: {media}") # exibe a média aritmética dos números da lista

