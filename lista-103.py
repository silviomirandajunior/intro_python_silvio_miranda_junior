#!/usr/bin/python3

'''
    DESAFIO!!!
    Implemente um algoritmo para inverter a ordem de uma string em sua
    linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

## STRINGS
## https://docs.python.org/3/tutorial/introduction.html#strings

msg = 'Minimal Techno Tripping'
size = len(msg)
print('Tamanho de msg:')
print(size)

## Converter para string
s = str(42)
print(s)

s = 'I like you'
print(s)

## Examine as strings colocando prints
s2 = s[0]  # retorna 'I'

s2 = len(s)  # retorna 10

# Como jah fizemos com as listas
s2 = s[0:7]  # retorna 'I like '

s2 = s[6:]  # retorna ' you'

s2 = s[-1]  # retorna 'u'


## concatenar strings
s3 = 'The meaning of life is'
s4 = '42'
s5 = s3 + ' ' + s4       # retorna 'The meaning of life is 42'
s5 = s3 + ' ' + str(42)  # same thing

# split a string into a list of substrings separated by a delimiter

s = 'Anything you want it to be'
s.split(' ')        # retorna ['Anything', 'you', 'want', 'it', 'to', 'be']
s.split()           # idem


# Entrada via teclado (caracter de escape -> '\')
print('What\'s your name?')
nome = input()
sobrenome = 'Abreu'
print('Hi, ' + nome)
print('Hi,', nome)

# Formatacao com o metodo format
msg = 'Hi, {} {}!'.format(sobrenome, nome)
print(msg)
msg = f'Hi, {sobrenome} {nome}!'
print(msg)


## Inverter a string
string = 'Hello, my friend!'
print(string)
string2 = string[::-1]
print(string2)

## Substituir
cheese_str = 'I like cheese'
print(cheese_str)
new_cheese_str = cheese_str.replace('like', 'love')
print(new_cheese_str)

###
# Exercicios
###


book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável

livro = book1.split(',')
ano1 = livro[1]
livro = book1.split('by')
print(livro[0])

livro2 = book2.split(',')
ano2 = livro2[1]
livro2 = book2.split('by')
print(livro2[0])

livro3 = book3.split(',')
ano3 = livro3[1]
livro3 = book3.split('by')
print(livro3[0])

# 3) Quantos caracteres cada título tem?

print(len(livro))
print(len(livro2))
print(len(livro3))

print(livro)
print(livro2)
print(livro3)

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}

titulo1 = livro[0]
titulo2 = livro2[0]
titulo3 = livro3[0]
autor1 = livro[1]
autor2 = livro2[1]
autor3 = livro3[2]


print("\n")
print("Titulo = {} \nAutor = {} \nAno = {}\n".format(titulo1, autor1, ano1))
print("Titulo = {} \nAutor = {} \nAno = {}\n".format(titulo2, autor2, ano2))
print("Titulo = {} \nAutor = {} \nAno = {}\n".format(titulo3, autor3, ano3))

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

palindrome_inverso = palindrome_one[::-1]

if(palindrome_inverso == palindrome_one):
	print("É um palindrome perfeito")
else:
	print("Não é um palindrome perfeito")

palindrome_inverso = palindrome_two[::-1]

if(palindrome_inverso == palindrome_two):
	print("É um palindrome perfeito")
else:
	print("Não é um palindrome perfeito")
	
palindrome_inverso = palindrome_three[::-1]

if(palindrome_inverso == palindrome_three):
	print("É um palindrome perfeito")
else:
	print("Não é um palindrome perfeito")

palindrome_inverso = palindrome_four[::-1]

if(palindrome_inverso == palindrome_four):
	print("É um palindrome perfeito")
else:
	print("Não é um palindrome perfeito")
