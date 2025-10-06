# Variável de controle do loop
saida = ""

# Funções matemáticas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível fazer a divisão por 0"
    else:
        return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    resultado = None

    if operacao in {"+", "adicao", "adição"}:
        resultado = adicao(num1, num2)
    elif operacao in {"-", "subtracao", "subtração"}:
        resultado = subtracao(num1, num2)
    elif operacao in {"*", "multiplicacao", "multiplicação"}:
        resultado = multiplicacao(num1, num2)
    elif operacao in {"/", "divisao", "divisão"}:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida!"

    return resultado

# Laço 
while saida.lower() != "n":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite apenas números válidos.")
        continue

    operacao = input("Digite a operação (+, -, *, / ou o nome da operação): ")

    resultado = calculadora(num1, num2, operacao)

    print("Resultado da operação:", resultado)

    saida = input("Deseja continuar? (S/N): ")

print("Programa encerrado!")
