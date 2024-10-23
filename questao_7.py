lista = [x for x in range(5)]
print(lista)

lista = list(range(5))
print(lista)

lista = []
i = 0
while i < 5:
    lista.append(i)
    i += 1
print(lista)



"""
- Saída:
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]

- Resposta Correta:
Letra D

- Resposta Marcada:
Letra D

- Reflexões:
a letra A funciona por list comprehension, bem compacta.
aparentemente range retorna um objeto que pode ser convertida em lista, fazendo com que a B funcione
a letra C funciona muito parecidamente com a letra A, e o while poderia ser substituido por um for loop

"""