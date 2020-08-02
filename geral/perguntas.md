# Perguntas

## Aula 1

1 - Qual é a função utilizada para imprimir algo na tela?
- puts()
- println()
- __print()__
- printf()

> A função é a print(). Basta passar a mensagem como parâmetro para a função, que a mensagem será impressa. Ela inclusive apareceu várias vezes no vídeo!

2 - Veja o código a seguir:
``` py
>>> subst = "Python"
>>> verbo = "é"
>>> adjetivo = "fantástico"
>>> print(subst, verbo, adjetivo, sep="_", end="!\n")
```
Qual será a saída do comando print?
- __Python_é_fantástico!__
- Python é fantástico!
- Python!é!fantástico_
- Python_é_fantástico

> Repare que usamos o parâmetro sep="_" para definir um _ entre cada valor, por isso é impresso:
> 
> ``` py
> Python_é_fantástico
> ```
> 
> Além disso, definimos através do end para imprimir uma exclamação (!), seguida pelo \n:
> 
> ``` py
> end="!\n"
> ```
> 
> Lembrando que o \n é um caractere especial, que faz com que o novo prompt comece em uma nova linha.
> 
> Com isso recebemos a saída:
> 
> ``` py
> Python_é_fantástico!
> >>>
> ```

3 - Para representar uma data, temos as variáveis dia, mes e ano:
``` py
>>> dia = 15
>>> mes = 10
>>> ano = 2015
```
Sem alterar as variáveis e sem passar nenhuma string adicional à função print(), como faríamos para ter como resultado da impressão, uma data formatada:

```
15/10/2015
```

Para ver a resposta do instrutor, basta clicar em Continuar.

- __print(dia, mes, ano, sep="/")__

> Podemos alterar o separador entre os valores que a função print() recebe, utilizando o parâmetro sep, que por padrão é um espaço em branco. Basta utilizá-lo, dizendo que seu valor será uma barra (/):
> ``` py
> >>> dia = 15
> >>> mes = 10
> >>> ano = 2015
> >>> print(dia, mes, ano, sep="/")
> 15/10/2015
> ```

4 - Temos a seguinte variável, que representa o preço de um produto:
``` py
preco = 49.99
```
Qual será o tipo da variável preco? Faça o teste!
- int
- double
- __float__
- decimal

> O valor 49.99, é um número decimal, ou seja, com um ponto flutuante, por isso em Python o seu tipo será o float. Podemos verificar isso no console do Python:
> ``` py
> >>> preco = 49.99
> >>> type(preco)
> <class 'float'>
> ```

5 - Sabendo que o Python usa uma tipagem dinâmica, qual alternativa abaixo é correta?
- __Uma variável só passa a existir quando atribuímos um valor.__
> Correto! É preciso atribuir um valor para inicializar uma variável, definindo assim o seu tipo.
- Uma variável passa a existir ao ser declarada, sem necessariamente termos atribuído um valor para ela, nem o tipo.
- Python permite declaração estática/explícita de variáveis.

> Não há declaração de variáveis estáticas em Python, como em linguagens como C, Java ou C#. Nessas linguagens, indicamos o tipo e o nome das variáveis e ela já passa a existir.
> Por exemplo:
> ``` py
> int idade;
> ```
> Repare que só declaramos o tipo e o nome da variável, sem ter atribuído o valor.
> Em Python, a variável só passa a existir quando atribuímos um valor, como no exemplo abaixo:
> ``` py
> idade = 12
> ```
> Isso faz todo sentido, já que não temos uma declaração explícita do tipo, como na linguagem Java ou C#. O interpretador do Python não tem como assumir um tipo.

## Aula 2

1 - Romário, seguindo o que foi aprendido neste curso, resolveu testar o código que compara o chute digitado pelo usuário com um número secreto definido no programa.
``` py
numero_secreto = 42
chute = input("Digite seu número")
print("Você digitou ", chute)
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")
```
Com base no código de Romário, temos as seguintes afirmações:

a) Sempre exibirá a mensagem Você errou, independentemente se o chute for igual ao número secreto

b) Todo valor retornado pela função input é um número.

c) É necessário converter o retorno de input para um número, no caso, um inteiro.

Sobre as afirmações anteriores, podemos dizer que:
- __Apenas B é falsa.__
- Apenas C é falsa.
- Apenas A é falsa.

> Não importa o número digitado, a comparação com == envolvendo tipos diferentes resultará em falso. Isso porque a função input sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro, para que a comparação com outro inteiro, no caso o numero_secreto, seja possível. Realizamos essa conversão através da função int.
> Corrigindo o código:
> ``` py
> numero_secreto = 42
> chute_str = input("Digite seu número")
> chute = int(chute_str)
> print("Você digitou ", chute)
> if(numero_secreto == chute):
>     print("Você acertou")
> else:
>     print("Você errou")
> ```
> No lugar de criarmos outra variável, usamos a mesma para receber o valor da sua conversão.

2 - Fernanda, colocando em prática o que aprendeu neste capítulo, escreveu o seguinte código para testar se realmente aprendeu a criar uma condição if em seu código:
``` py
minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado)
    print('temos idades iguais')
else:
    print('temos idades diferentes')
```
O problema é que o código dela não funciona. Consegue enxergar onde está o problema? Para quem está começando com Python, pode ser bem sutil. Descobriu? Clique em Ver Opinião do Instrutor, que você verá a resposta do instrutor.

- __Está faltando o ":" no final da linha do if__

>O problema é que para indicar o início do bloco if, é necessário utilizar dois pontos (:). Veja que no código dele faltou os dois pontos. O código corrigido ficará assim:
> ``` py
> minha_idade = 26
> idade_namorado = 25
> if(minha_idade == idade_namorado):
>     print('temos idades iguais')
> else:
>     print('temos idades diferentes')
> ```
> Importante também é sempre usar a indentação correta. Ou seja, depois da linha com o if, devemos usar 4 espaços ou pressionar a tecla tab para começar o novo bloco de código.

3 - Romeu fez uma simples comparação entre números, mas que não funciona. Segue o código:
``` py
numero1 = 10
numero2 = 10
if(numero1 = numero2):
    print("São números iguais")
```
Consegue descobrir onde Romeu errou? Pense bem para em seguida clicar em Ver Opinião do Instrutor e ver a resposta do instrutor.

- __Em vez de utilizar "==" ele utilizou "=" que significa atribuição em vez de ter usado o simbolo duplo que significa comparação__

> O problema é que foi usado um = para realizar a comparação. Quando usamos apenas um =, estamos atribuindo um valor à variável. Para compararmos valores ou variáveis, usamos o ==. Sendo assim, para o código do Romeu funcionar:
> ``` py
> numero1 = 10
> numero2 = 10
> if(numero1 == numero2):
>     print("São números iguais")
> ```

4 - Temos o seguinte código:
``` py
idade1 = 10
idade2 = "20"
print(idade1 + idade2)
```
Qual das opções abaixo possui o resultado do código? Fique à vontade de testar esse código no console do Python.
- "1020"
- 30
- __O código não funciona!__

> O código na verdade não funciona, e exibe a seguinte mensagem de erro no console:
> ``` py
> unsupported operand type(s) for +: 'int' and 'str'
> ```
> Isso acontece porque não podemos realizar uma operação de soma envolvendo uma string. Para resolvermos o problema, podemos apelar para a função int(), que converte uma string que contém um número, em um número inteiro:
> ``` py
> idade1 = 10
> idade2 = int("20")
> print(idade1 + idade2)
> ```

5 - Temos o seguinte trecho de código:
``` py
nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)
```
O resultado da operação é:
- Não é possível concatenar as duas variáveis.
- Nico Steppat
- __NicoSteppat__

> A resposta correta é NicoSteppat.
> O caractere + aqui não tem o significado de somar e sim de concatenar. Estamos concatenando (juntando) duas strings!
> Repare também que não há espaço entre as palavras. Para que haja, basta fazer assim:
> ``` py
> nome = "Nico"
> sobrenome = "Steppat"
> print(nome, sobrenome)
> ```
> Lembrando que a função print automaticamente aplica um separador entre os valores. O separador é um espaço por padrão, mas pode ser reconfigurado pelo parâmetro sep:
> ``` py
> nome = "Nico"
> sobrenome = "Steppat"
> print(nome, sobrenome, sep="_")
> ```

6 - Quais funções existem no Python 3?
- raw_input(..)
- __input(...)__
- __print(...)__
- __int(...)__

> As funções input(...), print(...) e int(...) existem no Python 3.
> A função raw_input(..) existe apenas no Python 2.

7 - Marque todas as alternativas verdadeiras:
- __No Python 3, a instrução print("ola", "mundo") imprime como saída ola mundo, diferente do Python 2, que possui como saída ('ola', 'mundo').__
- No Python 2, a função print aceita o parâmetro nomeado sep.
- __No Python 2, quando digitamos um valor numérico através de input, ele automaticamente converte de str para int. Já o Python 3 não assume essa conversão automática, sendo o desenvolvedor responsável por fazê-la.__
- __A função raw_input só existe em Python 2 e quando usada, lê a entrada como str, sem realizar conversões de tipos, como na função input.__
- __Uma função em Python 3 sempre deve possuir parênteses.__
