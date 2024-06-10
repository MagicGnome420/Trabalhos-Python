def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão  não é permitida."
    return x / y

def menu():
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

while True:
    menu()
    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha == '5':
        print("Vlw")
        break

    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("inválido, digite um número.")
            continue

        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            resultado = dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")

    else:
        print("Escolha inválida! Por favor, escolha uma opção de 1 a 5.")
