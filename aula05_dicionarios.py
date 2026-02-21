#Obs.: As chaves do diionário não podem ser iguais
dic_produtos = {'ipad':7000, 'iphone': 6000, 'airpod': 2000}

#Pegar um item
print(f'Valor do produto procurado: {dic_produtos['ipad']}') 

#Adicionar um item
dic_produtos['macbook'] = 12000
print(dic_produtos)

#Editar um item
dic_produtos['iphone'] = 8500
print(dic_produtos)

#Deletar um item
item_deletado = dic_produtos.pop('airpod')
print(f'Valor do item deletado: {item_deletado}')
print(dic_produtos)

#Verificar se item existe no dicionario
print('iphone' in dic_produtos)
print('iphone' in dic_produtos.keys()) #Especificando que a busca é pela chave, igual ao de cima.
print(7000 in dic_produtos.values()) #Especificando que a busca é pelo valor.