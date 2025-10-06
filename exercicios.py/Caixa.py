valor = int(input("digite um valor para sacar"))

if valor %5 !=0:
    print("valor deve ser multiplo de 5")

else:
    notas = [100, 50, 20, 10, 5]
    print("\n voce recebera")

for notas in notas:
    quantidades = valor // notas
    if quantidades > 0:
        print(f" {quantidades} de nota(s) r${notas}")

valor = valor % notas
