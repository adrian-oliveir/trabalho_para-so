# Importando os calculos para o menu.
import calculos

# Memória do sistema.
usuario_peso = 0.0
usuario_altura = 0.0
usuario_idade = 0
usuario_genero = ""

resultado_imc = 0.0
resultado_agua = 0.0
resultado_tbm = 0.0
meta_manter = 0.0
meta_ganhar = 0.0
meta_perder = 0.0
resultado_exercicio = ""


opcao_menu = -1

# Menu.
while opcao_menu != 0:
    print("\n" + "=" * 40)
    print("   SISTEMA DE SAÚDE & BEM-ESTAR")
    print("=" * 40)
    print("1 - Calcular IMC e Guardar Dados Básicos")
    print("2 - Calcular Meta de Hidratação")
    print("3 - Calcular TBM e Gasto Total")
    print("4 - Verificar Meta de Exercício")
    print("5 - 📄 GERAR RELATÓRIO FINAL")
    print("0 - Sair")

    opcao_menu = int(input("\nEscolha uma opção: "))

    # Opções do Menu.
    if opcao_menu == 1:
        print("\n--- 1. CÁLCULO DE IMC ---")
        usuario_peso = float(input("Digite seu peso (kg): "))
        usuario_altura = float(input("Digite sua altura (ex: 1.75): "))

        # Aqui guardamos o resultado do IMC
        resultado_imc = calculos.calcular_imc(usuario_peso, usuario_altura)
        print(f"Seu IMC foi calculado com sucesso: {resultado_imc:.2f}")

    elif opcao_menu == 2:
        print("\n--- 2. META DE HIDRATAÇÃO ---")

        if usuario_peso == 0.0:
            print("Aviso: Por favor, vá na Opção 1 primeiro para registrar seu peso!")
        else:
            resultado_agua = calculos.meta_hidratacao(usuario_peso)
            print(f"Sua meta diária é de {resultado_agua:.2f} litros de água.")

    elif opcao_menu == 3:
        print("\n--- 3. TBM E GASTO TOTAL ---")

        if usuario_peso == 0.0:
            print("Aviso: Por favor, vá na Opção 1 primeiro para registrar seu peso e altura!")
        else:
            usuario_idade = int(input("Digite sua idade: "))
            usuario_genero = input("Digite seu gênero (Masculino/Feminino): ")

            # Chamar nossa função TBM para ver o gênero do usuário.
            resultado_tbm = calculos.calcular_tbm(usuario_peso, usuario_altura, usuario_idade, usuario_genero)

            
            if resultado_tbm is None:
                print("Gênero não reconhecido. Tente novamente.")
            else:
                print("\nQual seu nível de atividade física?")
                print("1 - Sedentário")
                print("2 - Moderado")
                print("3 - Intenso")
                nivel = int(input("Escolha a opção (1/2/3): "))

                # A função retorna 3 valores, então recebemos os 3 em variáveis separadas
                meta_manter, meta_ganhar, meta_perder = calculos.calcular_gasto_total(resultado_tbm, nivel)
                print("Metas calóricas calculadas com sucesso! Vá para a Opção 5 para ver o relatório.")

    elif opcao_menu == 4:
        print("\n--- 4. META DE EXERCÍCIO ---")
        meta_min = int(input("Qual sua meta diária de exercícios (em minutos)? "))
        feito_min = int(input("Quantos minutos você já treinou hoje? "))

        resultado_exercicio = calculos.verificar_meta_exercicio(meta_min, feito_min)
        print(resultado_exercicio)

    elif opcao_menu == 5:
        print("\n" + "=" * 40)
        print("          RELATÓRIO DIÁRIO")
        print("=" * 40)
        print(f"Peso Registrado: {usuario_peso} kg")
        print(f"Altura Registrada: {usuario_altura} m")
        print("-" * 40)
        print(f"IMC Atual: {resultado_imc:.2f}")
        print(f"Meta de Água: {resultado_agua:.2f} L")

        # Só exibe as calorias se o usuário tiver feito a Opção 3
        if resultado_tbm > 0:
            print("-" * 40)
            print(f"Taxa Metabólica Basal: {resultado_tbm:.2f} kcal")
            print(f"Calorias para Manter: {meta_manter:.2f} kcal")
            print(f"Calorias para Ganhar: {meta_ganhar:.2f} kcal")
            print(f"Calorias para Perder: {meta_perder:.2f} kcal")

        if resultado_exercicio != "":
            print("-" * 40)
            print(f"Status do Treino: {resultado_exercicio}")

        print("=" * 40)

    elif opcao_menu == 0:
        print("\nEncerrando o sistema. Obrigado por utilizar!")

    else:
        print("\nOpção inválida! Por favor, escolha um número do menu.")
