def calcular_taxa_imposto(valor):
    if valor > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    return taxa


def calcular_imposto(lista_precos):
    imposto_total = 0
    for preco in lista_precos:
        taxa_imposto = calcular_taxa_imposto(preco)

        imposto = preco * taxa_imposto
        imposto_total += imposto
    
    return imposto_total


lista_precos = [1500, 1000, 800, 2000]
print(calcular_imposto(lista_precos))