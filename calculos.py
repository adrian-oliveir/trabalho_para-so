#Função para calcular imc;

def calcular_imc(peso, altura):
    return peso / (altura**2)

#Função para calcular a água.(Baseando-se em 35ml por kg);

def meta_hidratacao(peso):
    return peso * 0.035

"""
Funções para ver o usuário nas seguintes situações:
1- Taxa metabólica basal - TMB
2- Atividade leve
3- Atividade moderada
4- Atividade pesada 
"""

#Função TBM ( Masculino/feminino);

#Usando o método de Harris-Benedict para vermos diferença entre gênero para fazermos as funções;

def calcular_tbm(peso, altura, idade, genero):
    if genero.lower() == "masculino" :
        tbm = 88.36 + (13.4 * peso) + (4.8 * (altura * 100)) - (5.7 * idade)
    elif genero.lower() == "feminino" :
        tbm = 447.6 + (9.2 * peso) + (3.1 * (altura * 100)) - (4.3 * idade)
    else:
        return None
    return tbm

"""
Usando o métido Harris- Benedict vamos avaliar 2 pontos;
1- Termogênese da Atividade: Isso seria a análise de movimento voluntário (andar, limpar e etc) e na recuperação muscular.
2- Múltiplos da TMB: Os números TMB(1.2;1.55 e etc.) vão representar uma % sobre o aumento de gasto em repouso.
"""

#Calculo de intensidade de rotina do usuário;

def calcular_gasto_total(tbm,opcao):
    opcao_escolhida = opcao
    if opcao_escolhida == 1:
        fator = 1.2
        manter = tbm * fator
        print("Você escolheu o modo sedentário!")
    elif opcao_escolhida == 2:
        fator = 1.55
        manter = tbm * fator
        print(" Você escolheu o modo moderado! ")
    elif opcao_escolhida == 3:
        fator = 1.9
        manter = tbm * fator
        print("Você escolheu o modo intenso! ")
    else:
        return None
    ganhar_massa = manter + 500
    perca_massa = manter - 500
    return manter, ganhar_massa, perca_massa



