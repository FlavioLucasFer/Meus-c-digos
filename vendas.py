# FUNCIONALIDADE VENDAS
print('='*50)
menu = int(input('Digite 3: '))
if (menu == 3):
    print('='*50)
    print('''Escolha uma opção:
 1. Cadastrar Cliente
 2. Clientes Cadastrados
 3. Pendencias
 4. Vendas do Mês''')
print('-'*50)
menu = int(input('Opção escolhida: '))
print('-'*50)
    if (menu == 1):
        nome = str(input(' Nome: '))
        dtnasc = int(input(' Data de nascimento: '))
        print('-'*50)
        rua = input('Rua: ')
        bairro = input('Bairro: ')
        numero = int(input('Número: '))
        complemento = input('Complemento: ')
        print('-'*50)
        pagamento = input('Dia de pagamento: ')
        observacao = input('Observação: ')
        print('-'*50)
        print('Cliente {} cadastrado com sucesso!'.format(nome))
    elif (menu == 2):
        print('Em manutenção!')
    elif (menu == 3):
        print('Em manutenção!')
    elif (menu == 4):
        print('Em manutenção!')
    else:
        print('ERRO! Valor inválido foi inserido...')
print('='*50)
