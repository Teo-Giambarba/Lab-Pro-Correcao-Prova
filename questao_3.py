def func(n):
    if n == 0:
        return 1
    else:
        return n * func(n - 1)

print(func(3))

"""
- Saída:
6

- Resposta Correta:
6

- Resposta Marcada:
6

- Reflexões:
Essa função recursiva realiza o calculo do fatorial do número passado como parametro (func(n) = n! matematicamente).
o caso de parada da recursão é n ser igual a 0, e a recursão chama a mesma função mas com o n diminuido em 1, chegando eventualmente em 0
Essa função tem problemas com números negativos sendo passados, porque como chama func(n - 1) dentro de si mesma e checa por n ==0 um numero negativo nunca chega no caso de parada,
causando uma recursão infinita

"""