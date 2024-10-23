for i in range(1, 5):
    if i % 2 == 0:
        print(i, end="")

"""
- Saída:
2 4

- Resposta Correta:
2 4

- Resposta Marcada:
2 4

- Reflexões:
Esse código percorre os números no alcance de 1 a 4 e escreve o número com print se ele for par, substituindo o fim do print por " ", fazendo com que ele seja escrito na mesma linha.
É importante resssaltar que range(start, stop) inclui o parametro de inicio "start" mas exclui o de fim "stop", então range(1, 5) percorre de 1 a 4 na verdade.

"""