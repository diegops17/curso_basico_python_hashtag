lista = [] #Criando uma lista vazia

lista_mesclada = ['João', True, 22, 1.78, 'M']

lista_vendas = [100, 50, 1000, 800, 35]

print(f'Imprimir valor especifico da lista, passando o índice: {lista_vendas[1]}')

tamanho_lista = len(lista_vendas)
print(f'Tamanho da lista: {tamanho_lista}')
print(f'Último valor da lista: {lista_vendas[-1]}')


total_vendas = sum(lista_vendas)
print(f'Soma da lista: {total_vendas}')

print(f'Maior valor da lista: {max(lista_vendas)}')
print(f'Menor valor da lista: {min(lista_vendas)}')
print(f'Media da lista: {total_vendas / tamanho_lista}')

#Encontra valor na lista

lista_produtos = ['mouse', 'teclado', 'cpu', 'gpu']
#produto = str(input('Informe o produto para procurar na lista: ')).strip().lower()
#print(f'{produto}' in lista_produtos)

print(lista_produtos[3])

#Editar item na lista
lista_precos = [5000, 7000, 3000, 1000, 10000]
print(lista_precos)
novo_preco = lista_precos[2] * 1.1
lista_precos[2] = novo_preco
print(lista_precos)

#Remover item da lista
print(lista_produtos)
lista_produtos.remove('gpu')
print(lista_produtos)

item_removido = lista_produtos.pop(0)
print(lista_produtos)

#Adicionar item na lista
lista_produtos.append('notebook gamer')
print(lista_produtos)

lista_produtos.insert(0, 'headphone')
print(lista_produtos)

lista_produtos.extend(lista_mesclada)
print(lista_produtos)

#Contar quantos itens repetidos existe na lista
print(lista_produtos.count('mouse'))


#Ordenar lista
print(lista_precos)
lista_precos.sort()
print(lista_precos)

print(lista_vendas)
lista_vendas.sort(reverse=True)
print(lista_vendas)