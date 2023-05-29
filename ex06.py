#
#
# 6. (OBI 2016) Escreva um programa que receba uma lista de 
# números como entrada e exiba o maior número da lista.


#  solução 1
numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = list(map(int, numeros)) # converte a lista de strings para inteiros 
maior = max(numeros) # retorna o maior número da lista
print("O maior número da lista é:", maior)

# pq usar map?
# aplicar o print logo após o input.
print(max(list(map(int, input("Digite uma lista de números separados por espaço: ").split()))))

# solução 2
numeros = input("Digite uma lista de números separados por espaço: ").split()
maior = int(numeros[0]) # converte o primeiro número da lista para inteiro
for numero in numeros:
    if int(numero) > maior: # converte o número atual para inteiro
        maior = int(numero) # converte o número atual para inteiro
print("O maior número da lista é:", maior)
