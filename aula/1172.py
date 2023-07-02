lista = []
for i in range(10):
  numero = int(input())
  lista.append(numero)
for i in range(10):
  if lista[i] <= 0:
    lista[i] = 1
for i in range(10):
  print(f'X[{i}] = {lista[i]}')