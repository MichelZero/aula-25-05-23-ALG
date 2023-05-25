#
#
#
# https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci

# 2. (OBI 2020) Escreva um programa que leia um número 
# inteiro N e exiba os N primeiros termos da sequência 
# de Fibonacci.
# 0, 1, 1, 2, 3, 5, 8, 13, 21

n = int(input("Digite a quantidade de termos desejada: "))

ultimo=0
penultimo=0
termo = 1


for i in range(0,n):
  print(termo, ' ', end='')
  ultimo = penultimo
  penultimo = termo
  termo = ultimo + penultimo

