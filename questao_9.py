alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))
if alpha > 0.1:
    print("Valor inválido para alpha")
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)

"""
- Saída:
f(1,1): Valor invalido para alpha
f(0.10001,1): Valor invalido para alpha
 
f(0.1, 1) = 1.0
f(0, 5) = 5.0
f(0.5, 0.5) = Valor invalido para alpha
f(0.09, 0) = 0.0

f(0.1, -1) = -0.1
f(-1, -1) = 1.0
f(0, -10000) = -0.0
f(-3, -3) = 9.0
f(0.03, -0.1) = -0.003.0

- Resposta Correta:
Realizei os testes de mesa. Não dissertei se estava correto ou não

- Resposta Marcada:

-   -   Testes de mesa f(alpha,x) -   -
-   CASE: a invalido
f(1,1) = Valor invalido para alpha 
f(0.10001,1) = Valor invalido para alpha 

-   CASE: x >= 0, a valido
f(0.1, 1) = 1
f(0, 5) = 5
f(0.5, 0.5) = 5 # Erro meu, deveria ter retornado alpha invalido pois alpha > 0.1
f(0.09, 0) = 0

-   CASE: x < 0, a valido
f(0.1, -1) = -0.1
f(-1, -1) = 1
f(0, -10000) = 0
f(-3, -3) = 9
f(0.03, -0.1) = -0.003

- Reflexões:
Devido à pontuação e comentário do professor de "e ai? funciona?", eu
acredito que acertei todos os testes de mesa menos um, porém esqueci de dissertar se estava certo ou não (erro descuidado)
o código funciona corretamente para todos os casos testados, e não encontrei nenhum erro nele
f(0, -10000) resultou em -0 na saida do código, o que me surpreendeu pois não sabia que isso era permitido no python, porem aparentemente é efetivamente igual a 0 para os fins do teste.

"""