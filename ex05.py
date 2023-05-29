#
#
# 5. (OBI 2017) Escreva um programa que leia um número 
# inteiro N e exiba a soma de todos os números pares no 
# intervalo de 1 a N.

n = int(input("Digite um número inteiro: "))
soma = 0
for i in range(1, n+1):
    if i % 2 == 0:
        #soma += i
        soma = soma + i
print("A soma dos números pares é:", soma)
