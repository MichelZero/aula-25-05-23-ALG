#
#
# entrada de dados
soma = 0
for i in range(4):
  nota = int(input(f"informe a nota{i+1}: "))
  soma = soma + nota

media = soma / 4
print(f"a média foi: {media}")