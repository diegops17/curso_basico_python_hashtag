lista_vendas = [550, 330, 1100, 800, 9000, 17000, 15300, 6000]
total_vendas = sum(lista_vendas)

for venda in lista_vendas:
    if total_vendas >= 50000:
        if venda >= 15000:
            bonus = 500
            print(f'Bonus de R$ {bonus} reais.')
        elif venda >= 5000:
            bonus = 100
            print(f'Bonus de R$ {bonus} reais.')
        else:
            bonus = 0
            print(f'Bonus de R$ {bonus} reais.')
    else:
        print('Empresa não bateu a meta')
        break    
