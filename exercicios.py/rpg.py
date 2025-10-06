import random

def batalha(jogador, inimigo):
    print(f"\n⚔️ Você encontrou um {inimigo['nome']}!")

    while jogador["hp"] > 0 and inimigo["hp"] > 0:
        print(f"\nSeu HP: {jogador['hp']} | HP do {inimigo['nome']}: {inimigo['hp']}")
        acao = input("Você deseja (a) atacar ou (f) fugir? ").lower()

        if acao == "a":
            dano = random.randint(1, jogador["ataque"])
            inimigo["hp"] -= dano
            print(f"💥 Você causou {dano} de dano!")
        elif acao == "f":
            print("🏃 Você correu!")
            return False
        else:
            print("Opção inválida!")
            continue

        if inimigo["hp"] > 0:
            dano_inimigo = random.randint(1, inimigo["ataque"])
            jogador["hp"] -= dano_inimigo
            print(f"😈 O {inimigo['nome']} causou {dano_inimigo} de dano!")

    if jogador["hp"] > 0:
        print(f"\n🎉 Você derrotou o {inimigo['nome']}!\n")
        return True
    else:
        print("\n☠️ Você foi derrotado...")
        return False


# --- Jogador ---
jogador = {
    "nome": input("Digite o nome do seu herói: "),
    "hp": 30,
    "ataque": 8
}

# --- Lista de inimigos ---
inimigos = [
    {"nome": "Orc", "hp": 10, "ataque": 3},
    {"nome": "Goblin", "hp": 15, "ataque": 5},
    {"nome": "Bebê Dragão", "hp": 50, "ataque": 10}
]

print(f"\n👑 Bem-vindo à aventura, {jogador['nome']}!\n")

# --- Loop das batalhas ---
for inimigo in inimigos:
    vitoria = batalha(jogador, inimigo)
    if not vitoria:
        break

# --- Resultado final ---
if jogador["hp"] > 0:
    print(f"🏆 Parabéns, {jogador['nome']}! Você derrotou todos os inimigos!")
else:
    print("💀 Você foi derrotado...")
