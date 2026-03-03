import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
cod_resposta = requests.get(link)
print(cod_resposta)

cotacoes_moedas = cod_resposta.json()
print(cotacoes_moedas)

for moeda in cotacoes_moedas:
    valor_cotacao = cotacoes_moedas[moeda]['bid']
    print(f'{moeda} -> {valor_cotacao}')

