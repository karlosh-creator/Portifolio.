import pandas as pd
import matplotlib.pyplot as plt

# Ler o CSV
df = pd.read_csv("futebol_stats.csv")

print("📊 Estatísticas dos jogadores:")
print(df)

# Top 5 artilheiros
top_gols = df.sort_values(by="Gols", ascending=False).head(5)
print("\n⚽ Top 5 Artilheiros:")
print(top_gols[["Jogador", "Gols"]])

# Top 5 assistências
top_assistencias = df.sort_values(by="Assistencias", ascending=False).head(5)
print("\n🎯 Top 5 Assistências:")
print(top_assistencias[["Jogador", "Assistencias"]])

# Gráfico de gols por jogador
plt.bar(df["Jogador"], df["Gols"], color="green")
plt.title("Gols por Jogador")
plt.xlabel("Jogadores")
plt.ylabel("Gols")
plt.xticks(rotation=45)
plt.show()
