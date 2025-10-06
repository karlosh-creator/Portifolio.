banco = {}

def criar_conta(numeroconta, nome, saldo_inicial =0):
    if numeroconta in banco:
        print("conta ja existente")
    else:
        banco[numeroconta] = {"Nome": nome, "saldo": saldo_inicial, "extrato":[]}
        print(f"conta criada {nome} com r$: {saldo_inicial} de reais")


def depositar(numeroconta, valor):
    if numeroconta in banco:
        banco[numeroconta] ["saldo"] +=valor
        banco[numeroconta] ["extrato"].append(f"deposito de +R${valor}")
        print(f"deposito de R$ {valor} feito com sucesso!")
    else:
        print("conta não encontrada")


def sacar(numeroconta, valor):
    if numeroconta in banco:
        if banco[numeroconta] ["saldo"] >= valor:
            banco[numeroconta] ["saldo"] -= valor
            banco[numeroconta] ["extrato"].append(f"saque de -R${valor}")
            print(f"saque de R$ {valor} feito com sucesso!")
        else:
            print("saldo insuficiente")
    else:
        print("conta não encontrada")


def transferencia(origem, destino, valor):
    if origem in banco and destino in banco:
        if banco[origem] ["saldo"] >= valor:
         banco[origem] ["saldo"] -= valor
         banco[origem] ["extrato"].append(f"tranferencia de R${valor} para{destino} realizada com sucesso") 
         banco[destino] ["saldo"] += valor
         banco[destino ]["extrato"].append(f"transferencia recebida: =R${valor} com sucesso de {origem}!")
         print(f"tranferencia de {valor} de {origem} para {destino}")
        else:
            print("saldo insuficiente")
    
    else:
        print("conta não encontrada")


def saldo(numero):
    if numero in banco:
        print(f"saldo em conta {numero}: R$ {banco[numero]['saldo']}")
    else:
        print("conta não encontrada")

def extrato(numero):
    if numero in banco:
        print(f"extrato da conta{numero}")
        for mov in banco[numero]['extrato']:
            print("-", mov)
    else:
        print("conta não encontrada")


criar_conta(1, "carlos", 2500)
criar_conta(2, "Giuliana",2500)


depositar(1, 300)
extrato(1)
saldo(1)

transferencia (1, 2, 800)
extrato(2)
saldo(2)



    

                  


   










