#Bonus 1: R$ 2 reais por venda feita
#Bonus 2: 1% do valor de vendas
#Bonus de cada funcionario
#total de bonus 1 pago aos funcionarios
#total de bonus 2 pago aos funcionarios

def calcular_bonus(vendas):
    bonus1 = 2 * len(vendas)
    bonus2 = 0.01 * sum(vendas)

    return bonus1, bonus2


vendas = {
    'Andre': [1000, 500, 300, 5000, 1500, 80, 3000],
    'Andressa': [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    'Alan': [800, 100],
    'Ana': [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 60, 70, 70, 70, 200, 180, 100]
}

total_bonus1 = 0
total_bonus2 = 0

for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    print(f'{vendedor} teve BONUS1 1 de R$ {bonus1}, BONUS2 2 de R$ {bonus2}, TOTAL R$ {bonus1 + bonus2}')

    total_bonus1 += bonus1
    total_bonus2 += bonus2

    
print(f'Total bonus 1: {total_bonus1}')
print(f'Total bonus 2: {total_bonus2}')
print(f'Total bonus geral: {total_bonus1 + total_bonus2}')