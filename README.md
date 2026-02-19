# curso_basico_python_hashtag

Anotações:

Python é case sensitive;

*VARIAVEIS
Tipos;
-Números inteiros: int;
-Números com casas decimais: float;
-Textos: Strings;
-Booleanos: boolean (True, False);

*OPERADOES ARITMÉTICOS:
-Adição: +
-Subtração: -
-Multiplicação: *
-Divisão: /
-Mod (Resto da divisão): %
-Floor Division (Parte inteira da divisão): //


*OPERADORES LÓGICOS

-and
-or
------------------------------------------------
*STRING
.lower() - Tudo em minúscu
.upper() - lo. em caixa alta
.captalize() - Primeira letra da primeira palavra em caixa alta.
.title() - Coloca a primeira letra de cada palavra em caixa alta.
.strip() - Limpar espaços em branco.
len(nome_variavel) - Conta a quantidade de carateres da String.
.find('@') - Pega a posição do caractere.
.slice() - 
.replace('moto', 'carro') - Muda um texto por outro.


Exercicio:
1º Descobrir o servidor de e-mail.
2º Descobrir o primeiro nome do usuário.
3º Criar mensagem personalizada dizendo: Usuário tal (1º nome) foi cadastrado com sucesso no e-mail tal.
------------------------------------------------
*LISTAS
Obs: Lista em Python podem ter itens duplicados.

nome_lista = [] - Criar uma lista vazia.
nome_lista2 = () - Criar uma lista vazia.
lista_mista = ['João', 23, 1.89, 'M', True] - Lista em Python pode ter valores de tipos diferentes.

print(lista_mista[2]) - Pegar um determinado item da lista, passa a posição.
print(lista_mista[-1]) - Pegar o último item da lista, passa a posição -1, -2, etc.
print(lista_mista[3:]) -Pegar de determinada posição até o final da lista.

print(len(lista_mista)) - Pegar o tamanho da lista.

print('João' in lista_mista) - Verifica se um determinado item existe dentro da lista, retorna True se existir.
print(lista_mista.index('João')) -Pega o index de determinado item na lista.

-EDITAR um item na lista:
lista_mista[0] = 'João dos Santos'

-REMOVER um item da lista:
lista_mista.remove('M') -Passa o item que deseja remover, os metódos de remoção editam a lista in loco.
item_removido = lista.mista.pop(3) -Passa a posição do item que deseja remover. 

-INSERIR item na lista:
lista_mista('Brasil') -Adiciona um item no final da lista.
lista_mista.inset(2, 'Casado') -Inserir um item em uma posição especifica.
lista_mista.extend(nome_lista) -Adiciona os itens de uma lista dentro de outra lista, faz uma extensão.

-Contar quantas vezes um item aparece na lista:
print(lista_mista.cout('João'))

-Ordenar uma lista:
print(lista_mista.sort()) -Por padrão ordena em ordem crescente do a ao z, usa o modelo da tabela ASCII.
print(lista_mista.sort(reverse=True)) -Em ordem decrescente.
------------------------------------------------
*DICIONÁRIOS - Não pode ter duas chaves com o mesmo nome.

nome_dicionario = {} - Criar um dicionário vazio.

nome_dicionario2= {'nome': 'João', 'idade': 32, 'peso': 78.9}

print(nome_dicionario2['nome']) - Pegar o valor de um item.


-ADICIONAR UM ITEM
nome_dicionario2['sexo'] = 'M'

-EDITAR UM ITEM
nome_dicionario2['nome'] = 'João dos Santos'

-EXCLUIR UM ITEM
item_removido = nome_dicionario2.pop('idade') - Passa o nome da chave que quer excluir.
print(item_removido)

-VERIFICAR SE UMA CHAVE EXISTE NO DICIONÁRIO, RETORNA TRUE
print('nome' in nome_dicionario2)
print('nome' in nome_dicionario2.keys())


-VERIFICAR SE DETERMINADO VALOR EXISTE NO DICIONÁRIO, RETORNA TRUE.
print('João dos Santos' in nome_dicionario2.values())


len(nome_dicionario2) - Verificar tamanho d dicionário.

------------------------------------------------
*TUPLAS - São imutáveis

tupla_vendas = (1000, 800, 500)

print(tupla_vendas[1]) - Ver o valor.


def calcular_bonus(lista_vendas):
 bonus1 = 2 * len(lista_vendas)
 bonus2 = 0.01 * sum(lista_vendas)

 return bonus1, bonus2

vendas = [100, 250, 400, 1000]

#Unpacking da tupla a quantidade de retorno de valores, precisa ser igual a quantidade de variaveis passadas na chamada da função.
bonus1, bonus2 = calcular_bonus(vendas)

print(bonus1)
print(bonus2)



------------------------------------------------
*IF, ELSE, ELIF (Estruturas condicionais)

if condicao:
    executa esse trecho do código
else:
    se a condição or false cai aqui


if condicao:
    executa esse trecho do código
elif condicao 2:
    executa esse trecho do código
else:
    se a condição or false cai aqui


Exercicio:
-Vendas maiores que 15000, ganha bônus de 500
-Se as vendas forem entre 5000 e 15000, ganha bônus de 100
-Se as vendas forem menor que 500, não bônus

------------------------------------------------
*ESTRUTURAS DE REPETIÇÃO
*FOR*

for i in range(1, 10+1):
    print(i)


lista_precos = [1500, 1000, 800, 2000]

taxa_imposto = 0
total_imposto = 0

for preco in lista_precos:
    if preco > 1000:
        taxa_imposto = 0.15
    else:
        taxa_imposto = 0.1

    imposto = preco * taxa_imposto
    total_imposto += imposto
    print(f'Preço R$ {preco:.2f}, imposto R$ {imposto:.2f}')
print(f'Total de impostos R$ {total_imposto:.2f}')
------------------------------------------------
*FUNÇÕES

def nome_funcao(): #sem retorno.
    cód ser executado

def nome_funcao2(8, 2): #passando parametros.
    cód ser executado


def nome_funcao3(): #função com retorno.
    cód ser executado

    return alguma coisa


nome_funcao() #Chamando a função.
------------------------------------------------

*DICAS
15% é a mesma coisa de 0.15
Aumentar um item em 10%: item_desejado * 1.1
0.01 é a mesma coisa de 1%

