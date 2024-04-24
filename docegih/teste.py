def calcular_quantidade(valor, quantidade):
    gasto = quantidade * valor
    return gasto

def calcular_gasto_personalizado():
    peso_total = float(input("Qual o peso total do pacote (em gramas)? "))
    quantidade_utilizada = float(input("Quantos gramas você utilizou? "))

    valor_por_grama = valor / peso_total
    gasto = valor_por_grama * quantidade_utilizada

    return gasto

while True:
    print('\nESCOLHA O QUE DESEJA FAZER:\n [1] Calcular preço de ingrediente isolado\n [2]Calcular quanto ganhou em uma receita\n [3] Sair\n')
    esc = int(input())

    if esc == 1:
        ingrediente = input('Qual o ingrediente?\n')
        tipo = input('{} se conta em quantidade ou em gramas [q = quantidade // g = gramas]? '.format(ingrediente))
        valor = float(input('Qual o valor de {} (use pontos ao invés de vírgulas em decimais)? '.format(ingrediente)))
        
        if tipo == 'q':
            quantidade = int(input('Quantos {} foram usados? '.format(ingrediente)))
            gasto = calcular_quantidade(valor, quantidade)
            print ('Você vai gastar R$ {:.2f} em {} para fazer a receita!'.format(gasto, ingrediente))

        elif tipo == 'g':
            gasto_personalizado = calcular_gasto_personalizado()
            print ('Você vai gastar R$ {:.2f} em {} para fazer a receita!'.format(gasto_personalizado, ingrediente))

    elif esc == 2:
        pago = float(input('Quanto você gastou para fazer esse bolo? '))
        ganho = float(input('Quanto você ganhou na venda desse bolo? '))
        lucro = ganho - pago
        print('Você lucrou R${}! '.format(lucro))

    elif esc == 3:
        print('ENCERRANDO PROGRAMA...')
        break

    else:
        print('OPÇÃO INVÁLIDA, escolha dentre as opções listadas.')