faturamento = 1300
custo = 690
imposto = 0.15 * faturamento
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento
teve_lucro = True

print(f'Faturamento: R$ {faturamento}')
print(f'Custo: R$ {custo:.2f}')
print(f'Lucro: R$ {lucro:.2f}')
print(f'Margem de lucro: R$ {margem_lucro:.1%}')

print('*' * 20)

meses_financimento = 320

anos = int(meses_financimento / 12)
anos_2 = meses_financimento // 12

print(f'Anos de financiamento: {anos}')

meses = meses_financimento % 12
print(f'Restante de meses: {meses}')

print(f'Tempo total de financiamento {anos} anos e {meses} meses')
