# PlmcBks

Esta é uma biblioteca de código escrita em Python. Ela fornece vários meios de interagir com o nosso acervo de livros.

## Uso

Não sou bom documentando coisas, então irei demonstrar o uso desta biblioteca com explicações rápidas e uso prático.

- [Instalação](#instalação)
- [Tipos](#tipos)
  - [Dict](#1-dict)
  - [List](#2-list)
- [Entidades](#entidades)
  - [Navegação](#1-navegação-entre-entidades)
  - [Obtendo livros](#2-obtendo-livros-de-uma-entidade)
- [Livros](#livros)
  - [Pesquisa](#1-pesquisando-por-livros)


## Instalação

Você pode realizar a instalação usando o `pip`. É necessário que você possua pelo menos o Python 3.6 e um sistema operacional Linux para isso:

<details markdown='1'><summary>Código</summary>

```bash
python3 -m pip install --force-reinstall \
    --disable-pip-version-check \
    --no-warn-script-location \
    --user \
    --upgrade \
    'git+https://github.com/PolemicBooks/PlmcBks'
```

</details>

> As informações sobre todos os livros são armazenadas localmente em arquivos `json` e compactados usando o `xz`. Dependendo da sua máquina, pode demorar entre 5 a 10 minutos para que a biblioteca seja completamente importado durante uma sessão.

## Tipos

O PlmcBks possui 2 tipos principais, o `Dict` e o `List`. Eles são usados como base para todos os demais tipos (subclasses).

### 1. Dict

O `Dict` se baseia nos conceitos principais do tipo nativo `dict`. Você pode interagir com objetos desse tipo da seguinte forma:

<details markdown='1'><summary>Código</summary>

```python
from plmcbks.types import Dict

simple_dict = Dict()

# Associando valores 
simple_dict.foo = "bar"
simple_dict["bar"] = "foo"

# Exibindo valores
print(simple_dict.foo)
print(simple_dict["bar"])

# Excluindo valores
del simple_dict.foo
del simple_dict["bar"]
```

</details>

<details markdown='1'><summary>Resultado</summary>

```
bar
foo
```

</details>

<details markdown='1'><summary>Comentário</summary>

_Objetos desse tipo também podem ser facilmente convertidos para um dicionário usando o método nativo `dict()`._

</details>

### 2. List

O `List` se baseia nos conceitos principais do tipo nativo `list`. Você pode interagir com objetos desse tipo da seguinte forma:

<details markdown='1'><summary>Código</summary>

```python
from plmcbks.types import List

simple_list = List()

# Adicionando valores 
simple_list.append("bar")
simple_list.append("foo")

# Interagindo entre os valores
for item in simple_list:
    print(item)
```
</details>

<details markdown='1'><summary>Resultado</summary>

```
bar
foo
```

</details>

<details markdown='1'><summary>Comentário</summary>

_Objetos desse tipo também podem ser facilmente convertidos para listas usando o método nativo `list()`._

</details>

## Entidades

Entidades são objetos representado informações sobre um autor, narrador, editora e entre outros.

### 1. Navegação entre entidades

Veja abaixo alguns exemplos:

<details markdown='1'><summary>Código</summary>

```python
# Importamos todas as listas de entidades disponíveis
from plmcbks import (
    authors,
    artists,
    narrators,
    publishers,
    categories,
    types
)

# Exibimos o nome da primeira entidade presente na lista de autores.
print(authors[0].name)

# Exibimos o nome da primeira entidade presente na lista de artistas.
print(artists[0].name)

# Exibimos o nome da primeira entidade presente na lista de narradores.
print(narrators[0].name)

# Exibimos o nome da primeira entidade presente na lista de editoras.
print(publishers[0].name)

# Exibimos o nome da primeira entidade presente na lista de categorias.
print(categories[0].name)

# Exibimos o nome da primeira entidade presente na lista de tipos.
print(types[0].name)
```

</details>

<details markdown='1'><summary>Resultado</summary>

```
& e Décio Medeiros Carlos Castro
774 (Nanashi)
A Hora da História
#Incognitos
#StayAtHome
Audiobook
```

</details>

<details markdown='1'><summary>Comentário</summary>

Os demais atributos presentes em uma entidade são:

- `id`
  - Uma identificação numérica representando a posição em que a entidade em questão se encontra na lista.
- `total_books`
  - Uma identificação numérica representando a quantidade total de livros escritos, publicados, narrados ou presentes naquela entidade.

</details>

### 2. Obtendo livros de uma entidade

Cada entidade possui um método chamado `get_books()`. Quando chamado, ele retorna uma lista de todos os livros presentes nela.

No exemplo abaixo, usamos o `get_books()` para obter todos os livros do autor _Michael Withey_:

<details markdown='1'><summary>Código</summary>

```python
from plmcbks import authors, books

# Obtemos o objeto que representa o autor em questão
author = authors["Michael Withey"]

# Obtemos todos os seus livros
results = author.get_books(books)

# Interagimos entre os livros retornados
for book in results.iter():
    print(f"Title: {book.title}")
    print(f"Author: {book.author.name}")
    print(f"Type: {book.type.name}\n")

```

</details>


<details markdown='1'><summary>Resultado</summary>

```
Title: Descontruindo Seu Oponente: Como Identificar E Refutar Argumentos Falaciosos
Author: Michael Withey
Type: Ebook

Title: Descontruindo seu oponente: como identificar e refutar argumentos falaciosos
Author: Michael Withey
Type: Audiobook
```

</details>

<details markdown='1'><summary>Comentário</summary>

_Já que a dinâmica de obtenção de entidades é a mesma para todas as demais listas desse gênero, você também pode obter os livros de cada uma delas usando o mesmo método demonstrado acima._

</details>

## Livros

A partir daqui veremos exemplos sobre como pesquisar por livros e obter informações sobre documentos e imagens.

### 1. Pesquisando por livros

Veja os exemplos abaixo:

<details markdown='1'><summary>Código</summary>

```python
from plmcbks import books

# Pesquisa "rápida"
results_fast = books.fast_search("Python")

for book in results_fast.iter():
    print(f"Title: {book.title}")
    print(f"Author: {book.author.name}")
    print(f"Type: {book.type.name}\n")

# Pesquisa "lenta"
results_slow = books.slow_search("Python")

for book in results_slow.iter():
    print(f"Title: {book.title}")
    print(f"Author: {book.author.name}")
    print(f"Type: {book.type.name}\n")

```

</details>

<details markdown='1'><summary>Resultados</summary>


```
Title: A História (quase) Definitiva De Monty Python: Cinco Britânicos E Um Americano Que Reinventaram O Nonsense E Viraram O Mundo De Ponta-cabeça
Author: Thiago Meister Carneiro
Type: Ebook

Title: Python: Escreva Seus Primeiros Programas
Author: Felipe Cruz
Type: Ebook

Title: Trilhas Python: Programação Multiparadigma E Desenvolvimento Web Com Flask
Author: Eduardo Pereira
Type: Ebook

Title: Introdução À Visão Computacional: Uma Abordagem Prática Com Python E Opencv
Author: Felipe Barelli
Type: Ebook

Title: Consumindo A Api Do Zabbix Com Python
Author: Janssen Dos Reis Lima
Type: Ebook

Title: Aprenda Python Básico - Rápido e Fácil de entender
Author: Felipe Galvão
Type: Ebook

Title: Data Science do zero: Primeiras regras com o Python
Author: Joel Grus
Type: Ebook

Title: Curso Intensivo de Python
Author: Eric Matthes
Type: Ebook

Title: Python e Django
Author: Ramiro B. da Luz
Type: Ebook

Title: Python: Escreva seus primeiros programas
Author: Felipe Cruz
Type: Ebook

Title: Programação em Python: Introdução à programação com múltiplos paradigmas
Author: João Pavão Martins
Type: Ebook

Title: Python para Desenvolvedores
Author: Luiz Eduardo Borges
Type: Ebook

Title: Computação Científica com Python
Author: Flávio Codeço Coelho
Type: Ebook

Title: Pense em Python
Author: Allen B. Downey
Type: Ebook

Title: Introdução a Python - Módulo A
Author: Josué Labaki
Type: Ebook

Title: Introdução a Python - Módulo B
Author: Josué Labaki, Emanuel Woiski
Type: Ebook

Title: Aprendendo Python
Author: Mark Lutz/ David Ascher
Type: Ebook

Title: Automatize Tarefas Maçantes com Python
Author: Al Sweigart
Type: Ebook

Title: Data Science do Zero: Primeiras Regras Com o Python
Author: Joel Grus
Type: Ebook

Title: A Byte of Python
Author: Swaroop, C.H.
Type: Ebook
```

</details>

<details markdown='1'><summary>Comentário</summary>

As diferenças entre os dois métodos acima são:

1. Pesquisa lenta
> O método de pesquisa lenta exclui algumas palavras consideradas irrelevantes e também desconsidera a posição em que as palavras na pesquisa original aparecem.


2. Pesquisa rápida
> O método de pesquisa rápida, ao contrário do método de pesquisa lenta, não exclui palavras consideradas irrelevantes e também leva em conta a posição em que as palavras na pesquisa original aparecem.

A pesquisa lenta lhe trará resultados menos exatos, só que possivelmente mais relevantes.
A pesquisa rápida lhe trará resultados mais exatos, só que possivelmente menos relevantes.
