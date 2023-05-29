#
#
#
# 10. (OBI 2012) Escreva um programa que 
# receba uma string como 
# entrada e exiba o número de 
# vogais presentes na string.

palavra = input("Digite uma palavra: ") # entrada de dados
vogais = "aeiouAEIOU" # string com as vogais maiúsculas e minúsculas
contador = 0 # contador de vogais na palavra digitada pelo usuário 

for letra in palavra: # para cada letra na palavra digitada pelo usuário 
    if letra in vogais: # se a letra for uma vogal 
        contador += 1 # incrementa o contador de vogais 
        # contaro = contador + 1
print(f"Número de vogais: {contador}") # exibe o número de vogais na palavra digitada pelo usuário
