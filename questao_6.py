def soma_diagonal_principal_a(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

def soma_diagonal_principal_b(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][-i]
    return soma

def soma_diagonal_principal_c(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma

def soma_diagonal_principal_d(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz)-i-1]
    return soma

def soma_diagonal_principal_e(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[len(matriz)-i-1][i]
    return soma

matriz_teste = [[10, 5, 9],[1, 2, 7],[8, 3, 4]]
matriz_teste_anulada = [[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]
print(soma_diagonal_principal_a(matriz_teste_anulada))
print(soma_diagonal_principal_b(matriz_teste_anulada))
print(soma_diagonal_principal_c(matriz_teste_anulada))
print(soma_diagonal_principal_d(matriz_teste_anulada))
print(soma_diagonal_principal_e(matriz_teste_anulada))

"""
- Saída:
16
20
49
19
19

- Resposta Correta:
16 na soma (10 + 2 + 4), Letra A

- Resposta Marcada:
Letra A

- Reflexões:

A letra A realiza a soma dos seguintes indexes: 0 0, 1 1 e 2 2, que é a diagonal principal.
A letra B realiza a soma dos seguintes indexes: 0 0, 1 -1 (1 2) e 2 -2 (2 1), que faz uma retra que se traça do primeiro elemento e segue nos outros 2 elementos correspondentes,
pode ser util em calculo de determinante, eu acho
A letra B realiza a soma de todos os indexes, errando completamente a questão
A letra C realiza a soma dos seguintes indexes: 0 2, 1 1 e 2 0, que é a diagonal secundária
A letra D realiza a soma dos seguintes indexes: 2 0, 1 1 e 0 2, que é a diagonal secundario, porém pega seus elementos de tras pra frente, é identico em resultado a letra C

ou seja, apenas a letra A corresponde à resposta correta da implementação da funcionalidade.
"""