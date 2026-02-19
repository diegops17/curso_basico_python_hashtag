#1º Descobrir o servidor de e-mail.
email = str(input('Informe o seu e-mail completo: '))

inicio = email.find('@')
fim = email.find('.', inicio)
servidor = email[inicio + 1 : fim]

#print(inicio, fim)

#2º Descobrir o primeiro nome do usuário.
nome = str(input('Informe o seu nome completo: ')).upper().strip()

primeiro_nome = nome.split()
primeiro_nome = primeiro_nome[0]

#3º Criar mensagem personalizada dizendo: Usuário tal (1º nome) foi cadastrado com sucesso no e-mail tal.
mensagem = f'Usuário {primeiro_nome}, foi cadastrado com sucesso no e-mail do(a) {servidor}.'
print(mensagem)
