#
#
#

valores = input("informe números separados por espaço: ").split()
valor = list(map(int, valores))
media = sum(valor) / len(valor)
print(f"a média foi: {media}")