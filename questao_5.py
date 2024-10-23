def tem_duplicados_1(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def tem_duplicados_2(lista):
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
    return False

def tem_duplicados_3(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False

lista = [1, 3, 6, 9, 23, 56, 12, 4, 5, 2, 10, 11, 13, 339]
lista_dupe = [1, 3, 6, 9, 23, 56, 12, 4, 5, 2, 10, 11, 13, 339, 1]
print(tem_duplicados_1(lista))
print(tem_duplicados_2(lista))
print(tem_duplicados_3(lista))
print(tem_duplicados_1(lista_dupe))
print(tem_duplicados_2(lista_dupe))
print(tem_duplicados_3(lista_dupe))
"""
- Saída:
False
False
False
True
True
True

- Resposta Correta:
??? Pela minha revisão é a Letra D

- Resposta Marcada:
Letra D
Abordagem 1 é mais eficiente em espaço, mas menos eficiente em tempo

- Reflexões:

- Abordagem 1 -
Entre todas as abordagems, essa é a menos eficiente, ela percorre cada elemento da lista, e para cada elemento ela percorre a lista inteira novamnete, o que leva ela a ter uma
eficiencia de tempo de O(n²), porém ela utiliza de 0 espaço de memoria extra, sendo sua complexidade espaço O(1).

- Abordagem 2 -
Essa solução ordena a lista utilizando o método built-in do python, que é aparentemente O(n log n), e depois percorre pela lista inteira - 1,
comparando cada elemento com o proximo, adicionando uma complexidade de O(n - 1) para uma complexidade total de O(n log n + n - 1) que pode ser simplificada para O(n log n).
É mais eficiente que a abordagem 1, mas cria uma lista ordenada de complexidade espacial O(n), pois é do tamanho da lista original.

- Abordagem 3 -
A solução começa criando um conjunto vazio, e percorre a lista inteira com complexidade O(n), e para cada elemento que existe na lista ela observa se ele já esta presente no set,
o adicionando ao mesmo se não tiver. ela é a solução mais rápida, rodando em O(n), e também é bem eficiente em espaço, pois o set começa vazio e no melhor caso tem
Ω(1), mas no pior caso chega a ter O(n), melhor que a abordagem 2, que já cria a lista inteira de começo.

Analisando cada alternativa:
a) Abordagem 1 é a mais eficiente em tempo e espaço.
Ela é a menos eficiente em tempo de longe, por ser O(n²) contra O(n log n) e O(n), sendo essa alternativa FALSA

b) Abordagem 2 é a mais eficiente em tempo, mas consome mais espaço.
A Abordagem 3 consegue ser mais eficiente, pois é O(n), já a 2 é O(n log n). essa alternativa é FALSA

c) Abordagem 3 é a mais eficiente em tempo, mas consome mais espaço.
Ela é mais eficiente em tempo, porém consome menos espaço que a 2 em média por encher o conjunto enquanto executa. essa alternativa é FALSA

d) Abordagem 1 é a mais eficiente em espaço, mas menos eficiente em tempo.
A abordagem um tem consumo de espaço de O(1), porém ela é extremamente ineficiente em tempo, por ser O(n²). essa alternativa está CORRETA.

e) Abordagem 2 é a mais eficiente em espaço, mas menos eficiente em tempo.
A abordagem 2 é a menos eficiente em espaço, por sempre ter que usar uma lista do tamanho da lista original para ter complexidade espacial de O(n), e é mais eficiente do
que a abordagem 1, já que a 2 é O(n log n) contra a O(n²) da abordagem 1. essa alternativa é FALSA

Após correção, acredito que eu tenha acertado essa questão. pois foi marcada a letra D, que eu acredito ser a resposta correta.
"""