sair = False
voltar = True
voltar1 = True
deposito = 0
depositototal = 0
saque = 0
saldo = 0
saldomensal = 0
saldoanual = 0
contsaque = 0
contdeposito = 0
nome = 0
dtnasc = 0
rua = 0
bairro = 0
ncasa = 0
ntelefone = 0
ncelular = 0
email = 0
pagamento = 0
modalidade = 0
cliente = nome, dtnasc, rua, bairro, ncasa, ntelefone, ncelular, email, pagamento, modalidade
while (sair == False):
    print('''==========================< Menu >==========================
 1. Depositar
 2. Sacar
 3. Saldo
 4. Extrato
 5. Vendas / Sobrancelhas
 6. Sair''')
    menu = int(input(' Opção escolhida: '))
    if (menu == 6):
        print('-'*60)
        print(' Muito obrigado por utilizar o software! S2')
        sair = True

# implemento 1: Depositar
# status do implemento: totalmente pronto e funcionando corretamente

    while (menu == 1):
        voltar = True
        voltar1 = True
        print('-----------------------< Depositar >------------------------')
        deposito = float(input('\n Quantos reais deseja depositar? R$'))
        depositototal = depositototal + deposito
        while (voltar == True):
            print('\n 1. Confirmar             2. Corrigir            3. Cancelar')
            print('-'*60)
            confirm = int(input(' Opção escolhida: '))
            if (confirm == 1):
                contdeposito = contdeposito + 1
                print('-'*60)
                print(' Depósito de R${} efetuado com sucesso!'.format(deposito))
                print('-'*60)
                while (voltar1 == True):
                    print(' 1. Voltar para o menu príncipal\n 2. Sair')
                    print('-'*60)
                    escolha = int(input(' Opção escolhida: '))
                    if(escolha == 1):
                        voltar1 = False
                        voltar = False
                        menu = 0
                        sair = False
                    elif (escolha == 2):
                        print('-'*60)
                        print(' Muito obrigado por utilizar o software! S2')
                        sair = True
                        menu = 0
                        voltar = False
                        voltar1 = False
                    else:
                        print('-'*60)
                        print('Valor inválido, tente novamente!')
                        print('-'*60)
            elif (confirm == 2):
                depositototal = depositototal - deposito
                voltar = False
                menu = 1
            elif (confirm == 3):
                deposito = 0
                print('-'*60)
                print('                    > Operação cancelada! <')
                while (voltar1 == True):
                    print('-'*60)
                    print(' 1. Voltar para o menu príncipal\n 2. Sair')
                    print('-'*60)
                    escolha = int(input(' Opção escolhida: '))
                    if(escolha == 1):
                        voltar1 = False
                        voltar = False
                        menu = 0
                        sair = False
                    elif (escolha == 2):
                        print('-'*60)
                        print(' Muito obrigado por utilizar o software! S2')
                        sair = True
                        menu = 0
                        voltar = False
                        voltar1 = False
            else:
                print('-'*60)
                print('Valor inválido, tente novamente!')
                print('-'*60)
                voltar = True

# implemento 2: Sacar
# status do implemento: totalmente pronto e funcionando corretamente

    while (menu == 2):
        voltar = True
        voltar1 = True
        saldo = depositototal - saque
        print('--------------------------< Sacar >-------------------------')
        print('\n                  Seu saldo atual é de {}'.format(saldo))
        saque = float(input('\nQuanto deseja sacar? R$'))
        while (voltar == True):
            print('\n 1. Confirmar             2. Corrigir            3. Cancelar')
            print('-'*60)
            confirm = int(input(' Opção escolhida: '))
            if (confirm == 1):
                print('-'*60)
                print(' Saque de R${} efetuado com sucesso!'.format(saque))
                saldo = deposito - saque
                contsaque = contsaque + 1
                print('-'*60)
                while (voltar1 == True):
                    print(' 1. Voltar para o menu príncipal\n 2. Sair')
                    print('-'*60)
                    escolha = int(input(' Opção escolhida: '))
                    if(escolha == 1):
                        voltar1 = False
                        voltar = False
                        menu = 0
                        sair = False
                    elif (escolha == 2):
                        print('-'*60)
                        print(' Muito obrigado por utilizar o software! S2')
                        sair = True
                        menu = 0
                        voltar = False
                        voltar1 = False
                    else:
                        print('-'*60)
                        print(' Valor inválido, tente novamente!')
                        print('-'*60)
            elif (confirm == 2):
                saldo = 0
                saque = 0
                voltar = False
                menu = 2
            elif (confirm == 3):
                saque = 0
                print(' 1. Voltar para o menu príncipal\n 2. Sair')
                print('-'*60)
                escolha = int(input(' Opção escolhida: '))
                if(escolha == 1):
                    voltar1 = False
                    voltar = False
                    menu = 0
                    sair = False
                elif (escolha == 2):
                    print('-'*60)
                    print(' Muito obrigado por utilizar o software! S2')
                    sair = True
                    menu = 0
                    voltar = False
                    voltar1 = False
            else:
                print('-'*60)
                print(' Valor inválido, tente novamente!')
                print('-'*60)
                voltar = True

# implemento 3: Saldo
# status do implemento: em progresso

    while (menu == 3):
        voltar = True
        voltar1 = True
        print('--------------------------< Saldo >-------------------------')
        print('''1. Saldo Atual
2. Saldo Mensal
3. Saldo Anual
4. Saldo comparação''')
        escolha = int(input('Opção escolhida: '))
        while (escolha == 1):
            saldo = depositototal - saque
            print('----------------------< Saldo Atual >-----------------------')
            print('\n               < Seu saldo atual é de {} >\n'.format(saldo))
            while (voltar1 == True):
                print(' 1. Voltar para o menu príncipal\n 2. Sair')
                print('-'*60)
                escolha = int(input(' Opção escolhida: '))
                if(escolha == 1):
                    voltar1 = False
                    escolha = 0
                    menu = 0
                    sair = False
                elif (escolha == 2):
                    print('-'*60)
                    print(' Muito obrigado por utilizar o software! S2')
                    sair = True
                    menu = 0
                    voltar = False
                    voltar1 = False
                else:
                    print('-'*60)
                    print(' Valor inválido, tente novamente!')
                    print('-'*60)

# implemento 4: Extrato
# status do implemento: em progresso

    while (menu == 4):
        saldo = depositototal - saque
        saldomes = saldo
        saldoanual = saldomes
        print('------------------------< Extrato >-------------------------')
        print(''' Neste mês você efetuou {} saques e {} depósitos
\n Seu saldo atual é de {}
\n Seu saldo do mês foi de {}
\n Seu saldo Anual foi de {}
 '''.format (contsaque, contdeposito, saldo, saldomes, saldoanual))
        while (voltar == True):
            print('-'*60)
            print(' 1. Voltar para o menu príncipal\n 2. Sair')
            print('-'*60)
            escolha = int(input(' Opção escolhida: '))
            if(escolha == 1):
                voltar = False
                menu = 0
                sair = False
            elif (escolha == 2):
                print('-'*60)
                print(' Muito obrigado por utilizar o software! S2')
                sair = True
                menu = 0
                voltar = False
            else:
                print('-'*60)
                print(' Valor inválido, tente novamente!')
                print('-'*60)

# implemento 5: Vendas / Sobrancelhas
# status do implemento: em progresso

    while (menu == 5):
        print('-----------------< Vendas / Sobrancelhas >------------------')
        print(''' 1. Cadrastar Cliente
 2. Alterar Cadastro
 3. Exibir Cadastro
 4. Adicionar venda
 5. Sair''')
        print('-'*60)
        escolha = int(input(' Opção escolhida: '))
        while (escolha == 1):
            print('-------------------< Cadastrar Cliente >--------------------')
            print(' Informações pessoais\n')
            nome = str(input(' Nome: '))
            dtnasc = str(input(' Data de nascimento: '))
            print('-'*60)
            print(' Endereço\n')
            rua = str(input(' Rua: '))
            bairro = str(input(' Bairro: '))
            ncasa = int(input(' Número da casa: '))
            print('-'*60)
            print(' Contato\n')
            ntelefone = str(input(' Número de telefone: '))
            ncelular = str(input(' Número de celular: '))
            email = str(input(' E-mail: '))
            print('-'*60)
            print(' Pagamento e modalidade\n')
            pagamento = int(input(' Dia de preferência do pagamento: '))
            modalidade = str(input(' Modalidade do cliente: '))
            while (voltar == True):
                print('\n 1. Confirmar             2. Corrigir            3. Cancelar')
                print('-'*60)
                confirm = int(input(' Opção escolhida: '))
                if (confirm == 1):
                    print('-'*60)
                    print(' Cadastro do cliente {} realizado com sucesso!'.format(nome))
                    print('-'*60)
                    while (voltar1 == True):
                        print(' 1. Voltar para o menu príncipal\n 2. Sair')
                        print('-'*60)
                        escolha = int(input(' Opção escolhida: '))
                        if(escolha == 1):
                            voltar1 = False
                            voltar = False
                            menu = 0
                            sair = False
                        elif (escolha == 2):
                            print('-'*60)
                            print(' Muito obrigado por utilizar o software! S2')
                            sair = True
                            menu = 0
                            voltar = False
                            voltar1 = False
                        else:
                            print('-'*60)
                            print(' Valor inválido, tente novamente!')
                            print('-'*60)
                elif (confirm == 2):
                    saldo = 0
                    saque = 0
                    voltar = False
                    menu = 2
                elif (confirm == 3):
                    saque = 0
                    print(' 1. Voltar para o menu príncipal\n 2. Sair')
                    print('-'*60)
                    escolha = int(input(' Opção escolhida: '))
                    if(escolha == 1):
                        voltar1 = False
                        voltar = False
                        menu = 0
                        sair = False
                    elif (escolha == 2):
                        print('-'*60)
                        print(' Muito obrigado por utilizar o software! S2')
                        sair = True
                        menu = 0
                        voltar = False
                        voltar1 = False
                else:
                    print('-'*60)
                    print(' Valor inválido, tente novamente!')
                    print('-'*60)
                    voltar = True
cliente = nome, dtnasc, rua, bairro, ncasa, ntelefone, ncelular, email, pagamento, modalidade
print(cliente)
print('='*60)
