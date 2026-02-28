tupla_vazia = ()
tupla_vendas = (1000, 800, 500)

print(tupla_vendas[1])

print('*' * 50)
#Bonus 1: R$ 2 reais por venda feita
#Bonus 2: 1% do valor de vendas

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)

    return bonus1, bonus2


vendas = [100, 250, 400, 1000]

resultado = calcular_bonus(vendas)
print(resultado)

print('*' * 50)

bonus_01 = resultado[0]
bonus_02 = resultado[1]
print(bonus_01)
print(bonus_02)

print('*' * 50)
#Unpacking da tupla
bonus1, bonus2 = calcular_bonus(vendas) 

lisa_telas = [(1090, 1080),(2140, 1080)]

for altura, largura in lisa_telas:
    print(f'Altura: {altura} X Largura: {largura}')