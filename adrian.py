opção = int(input('escolha uma opção'))

if opção == 1:
    peso = float(input('digite seu peso'))
    altura = float(input('digite sua altura'))
    imc = peso / (altura * altura)
    print('seu imc é:', imc)

    if imc < 18.5:
        print('abaixo do peso')
    elif imc < 25:
        print('peso normal')
    elif imc < 30:
        print('sobre peso')
    else:
        print('obesidade')

elif opção == 2:
     peso = float(input('digite seu peso'))
     agua = peso * 35
     print('essa é a quantidade de água que você deve beber: ', agua)

elif opção == 3:
    tempo = int(input('quantos minutos de exercicios você fez hoje?'))
    calorias = tempo * 5
    print('essas são as calorias que você perdeu hoje: ', calorias)

elif opção == 4:
    meta = float(input('digite sua meta em minutos'))
    tempo_hoje = float(input('digite quanto tempo de exercícios você fez hoje em minutos'))
    if tempo_hoje >= meta:
        print('meta atingida')
    else:
        print('meta não atingida')

elif opção == 0:
    print('sair')

else:
    print('não foi selecionado nenhuma das opções')

