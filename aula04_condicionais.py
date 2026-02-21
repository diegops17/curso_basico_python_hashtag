faturamento = 1000
custo = 600
lucro = faturamento - custo

if lucro >= 0:
    print(f'Lucro de R$ {lucro} reais')

else:
    print(f'Pejuízo de R$ {lucro} reais')

lista_produtos = ['mouse', 'teclado', 'gpu']

produto = str(input('Informe o nome do produto: ')).strip().lower()

if produto in lista_produtos:
    print(f'Produto {produto} já possui cadastro.')
else:
    lista_produtos.append(produto)
    print(f'Produto {produto} cadastrado com sucesso.')

print(lista_produtos)