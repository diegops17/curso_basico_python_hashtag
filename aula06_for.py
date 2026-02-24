lista_precos = [1500, 1000, 800, 2000]

taxa_imosto = 0.1

for preco in lista_precos:
    imposto = preco * taxa_imosto
    print(f'Preço do produto R$ {preco}, imposto é de R$ {imposto}') 

print('*' * 50)

for i in range(1, 10+1):
    print(i)

print('*' * 50)

for i in range(5):
    print(i)

print('*' * 50)

vendas_24 = {'jan': 15000, 'fev': 10000, 'mar': 5000}
vendas_25 = {'jan': 16000, 'fev': 11000, 'mar': 5100}

for mes in vendas_24:
    valor_24 = vendas_24[mes]
    valor_25 = vendas_25[mes]

    crescimento = valor_25 / valor_24 - 1

    print(f'No mês de {mes} o crescimento foi de {crescimento:.1%}') 