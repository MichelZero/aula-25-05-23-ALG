#
#
#
# 4. (OBI 2018) Escreva um programa que receba um número 
# inteiro N como entrada e exiba todos os números 
# primos menores que N.

num = int(input("Informe um número inteiro: "))

for i in range(1, num+1): 
    cont = 0 # contador de divisores de i 
    for k in range(1, i+1): 
        if i % k == 0: # se i for divisível por k 
            cont += 1 # incrementa o contador de divisores de i 
    if cont == 2: # se i tiver exatamente 2 divisores 
        print(i, ' ', end='') # imprime i