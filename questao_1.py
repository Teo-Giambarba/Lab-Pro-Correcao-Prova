a = '5'
b = 2
c = a * b
print(c)

"""
- Saída:
55

- Resposta Correta:
'55'

- Resposta Marcada:
'55'

- Reflexões:
Apesar de o comando print excluir as aspas, podemos verificar que o valor de c é uma string ao usar print(type(c)), determinando que a respota correta seja '55'.
A saida ocorre porque Python tem suporte para a multiplicação de strings por inteiros, que resulta em a string sendo repetida a quantidade de vezes que o numero inteiro representar.
Esse comportamento de multiplicação de strings por int é consistente em qualquer string que voce multiplicar por um numero inteiro, fazer 'O' * 5, por exemplo, vai resulta em 'OOOOO'
"""