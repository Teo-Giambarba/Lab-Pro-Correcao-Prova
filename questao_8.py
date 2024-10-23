peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura em cm: "))/100
IMC = peso/(altura ** 2)
print(f"seu IMC é {IMC}")
classe = ""
if IMC < 17:
    classe = "Muito Abaixo do peso"
elif IMC < 18.5:
    classe = "Abaixo do Peso"
elif IMC < 25:
    classe = "Peso Normal"
elif IMC < 30:
    classe = "Sobrepeso"
elif IMC < 35:
    classe = "Obesidade Grau I"
elif IMC < 40:
    classe = "Obesidade Grau II"
else:
    classe = "Obesidade Grau III"
print(f"sua classificação é {classe}")
"""
- Saída:
(peso = 70, altura = 182)
seu IMC é 21.132713440405748
sua classificação é Peso Normal

- Resposta Correta:
Discursiva, porém o resultado está correto

- Resposta Marcada:
Discursiva

- Reflexões:
Esse código me parece bem repetitivo, se possível gostaria de tentar fugir dessa camada de if/elifs pra verificar qual é a sua classe
pode ser apenas neurose, pois é um caso bem simples. Eu vejo a possibilidade de utilizar um dicionario para fazer essas verificações
eu deveria ter juntado as duas partes em um único print também

"""