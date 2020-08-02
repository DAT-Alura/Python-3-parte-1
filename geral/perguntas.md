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
