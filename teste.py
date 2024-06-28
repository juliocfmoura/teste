def analisador_sequencia():
    # Inicializar a lista de números
    numeros = []

    # Loop para inserir números
    while True:
        entrada = input("Digite um número inteiro (ou 'sair' para finalizar): ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    if len(numeros) == 0:
        print("Nenhum número foi inserido.")
        return

    # Calcular a soma dos números
    soma = sum(numeros)

    # Calcular a média dos números
    media = soma / len(numeros)

    # Encontrar o maior e o menor número
    maior = max(numeros)
    menor = min(numeros)

    # Contar positivos, negativos e zeros
    positivos = len([num for num in numeros if num > 0])
    negativos = len([num for num in numeros if num < 0])
    zeros = len([num for num in numeros if num == 0])

    # Exibir os resultados
    print("\nResultados da Análise:")
    print(f"Números inseridos: {numeros}")
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")
    print(f"Zeros: {zeros}")

# Executar o programa
analisador_sequencia()
