#Produto de até 1000 reais 10%
#Produto acima de 1000 reais 15%
#Calcular o total de imposto somando todos os produtos

lista_precos = [1500, 1000, 800, 2000]

total_imposto = 0

for preco in lista_precos:
    if preco <= 1000:
        taxa_imposto = 0.1
    else:
        taxa_imposto = 0.15
    imposto = preco * taxa_imposto
    total_imposto += imposto

    print(f'Preço do produto R$ {preco}, taxa de imposto {taxa_imposto:.0%} imposto é de R$ {imposto}')
print(f'Total de imposto somanto todos os produtos R$ {total_imposto} reais')