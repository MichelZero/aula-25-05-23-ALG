#
#
# 3. (OBI 2019) Escreva um programa que receba uma string 
# como entrada e verifique se ela é um palíndromo.

palavra = input("Digite uma palavra: ")

invertida = palavra[::-1]

if palavra == invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
