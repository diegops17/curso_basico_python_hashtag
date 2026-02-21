dic_produtos = {'ipad':7000, 'iphone': 6000, 'airpod': 2000}

item_procurado = str(input('Informe o nome do item: ')).strip().lower()

if item_procurado in dic_produtos:
    print(f'Item {item_procurado} já possui cadastro. Valor R$ {dic_produtos[item_procurado]} reais')
else:
    opcao = str(input(f'Item {item_procurado} não possui cadastro. Deseja cadastrar [S/N]? ')).strip().lower()[0]

    if opcao == 's':
        valor = float(input('Informe o valor do produto R$ '))
        dic_produtos[item_procurado] = valor
        print(f'{item_procurado} cadastrado com sucesso.')

    elif opcao == 'n':
        print('Obrigado, volte sempre.')

    else:
        print('ERRO: Opção inválida, escolha [S/N]')

print('****** CADASTRO COMPLETO ******')
print(dic_produtos)