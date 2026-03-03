import os

#Mostrar o caminho onde tá o código
#print(os.getcwdb()) 

#Listar arquivos dentro do diretorio
#print(os.listdir())

lista_arquivos = os.listdir('arquivos')
print(lista_arquivos)

for nome_arquivo in lista_arquivos:
    if 'txt' in nome_arquivo:
        if '24' in nome_arquivo:
            os.rename(f'arquivos/{nome_arquivo}', f'arquivos/24/{nome_arquivo}')
        elif '25' in nome_arquivo:
            os.rename(f'arquivos/{nome_arquivo}', f'arquivos/25/{nome_arquivo}')