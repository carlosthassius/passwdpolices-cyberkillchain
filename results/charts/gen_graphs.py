import matplotlib.pyplot as plt
import pandas as pd

# Dados completos
data = {
    "File": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Password": ["0OhBycb9wKT0rEO", "0HflID2LmYnu3fY", "JohnSmith123#", "John@2024", "John123", "john123", "John", "john", "45562", "25122024", "12345", "987654321"],
    "Length (s)": [3600, 3600, 3600, 3600, 3600, 6.81, 0.21, 0.22, 3600, 3600, 0.22, 0.23],
    "Incremental (s)": [3600, 3600, 3600, 3600, 3600, 3600, 3600, 0.733, 11.409, 25.458, 0.116, 66.764],
    "Incremental + Length (s)": [3600, 3600, 3600, 3600, 3600, 24.93, 6.87, 0.16, 0.96, 2.8, 0.1, 0.8],
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Substituindo valores > 3600 por 0 para nivelar as barras
df["Length (s)"] = df["Length (s)"].replace(3600, 0)
df["Incremental (s)"] = df["Incremental (s)"].replace(3600, 0)
df["Incremental + Length (s)"] = df["Incremental + Length (s)"].replace(3600, 0)

# Arredondando os valores para uma casa decimal
df["Length (s)"] = df["Length (s)"].round(1)
df["Incremental (s)"] = df["Incremental (s)"].round(1)
df["Incremental + Length (s)"] = df["Incremental + Length (s)"].round(1)

# Selecionando os dados sem as primeiras 5 senhas
df_new = df[5:].reset_index(drop=True)

# Criando o gráfico com duas partes (3 senhas em cima e 4 em baixo)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12))

# Primeiros 3 dados no gráfico superior
x1 = range(3)
ax1.bar([i + 0.25 for i in x1], df_new["Incremental (s)"][:3], width=0.25, label="Alphabet", alpha=1.0, color="orange")
ax1.bar(x1, df_new["Length (s)"][:3], width=0.25, label="Length", alpha=1.0, color="blue")
ax1.bar([i + 0.5 for i in x1], df_new["Incremental + Length (s)"][:3], width=0.25, label="Alphabet & Length", alpha=1.0, color="green")
ax1.set_xticks([i + 0.25 for i in x1])
ax1.set_xticklabels(df_new["Password"][:3], rotation=0, ha="center", fontsize=14)  # Aumentando o tamanho da fonte
ax1.set_ylabel("Time (seconds)", fontsize=16)
ax1.legend(fontsize=14)  # Aumentando o tamanho da legenda

# Adicionando os rótulos de valor no gráfico superior
for i, bar in enumerate(ax1.bar(x1, df_new["Length (s)"][:3], width=0.25)):
    height = bar.get_height()
    label = f'{height}' if height != 0 else '> 3600s'  # Ajuste para mostrar '> 3600s' quando for 0
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, label, ha='center', va='bottom', fontsize=12, color='black')

for i, bar in enumerate(ax1.bar([i + 0.25 for i in x1], df_new["Incremental (s)"][:3], width=0.25)):
    height = bar.get_height()
    label = f'{height}' if height != 0 else '> 3600s'  # Ajuste para mostrar '> 3600s' quando for 0
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, label, ha='center', va='bottom', fontsize=12, color='black')

for i, bar in enumerate(ax1.bar([i + 0.5 for i in x1], df_new["Incremental + Length (s)"][:3], width=0.25)):
    height = bar.get_height()
    label = f'{height}' if height != 0 else '> 3600s'  # Ajuste para mostrar '> 3600s' quando for 0
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, label, ha='center', va='bottom', fontsize=12, color='black')

# Últimos 4 dados no gráfico inferior
x2 = range(3, 7)
ax2.bar([i + 0.25 for i in x2], df_new["Incremental (s)"][3:], width=0.25, label="Alphabet", alpha=1.0, color="orange")
ax2.bar(x2, df_new["Length (s)"][3:], width=0.25, label="Length", alpha=1.0, color="blue")
ax2.bar([i + 0.5 for i in x2], df_new["Incremental + Length (s)"][3:], width=0.25, label="Alphabet & Length", alpha=1.0, color="green")
ax2.set_xticks([i + 0.25 for i in x2])
ax2.set_xticklabels(df_new["Password"][3:], rotation=0, ha="center", fontsize=14)  # Aumentando o tamanho da fonte
ax2.set_xlabel("Password", fontsize=16)
ax2.set_ylabel("Time (seconds)", fontsize=16)

# Adicionando os rótulos de valor no gráfico inferior
for i, bar in enumerate(ax2.bar(x2, df_new["Length (s)"][3:], width=0.25)):
    height = bar.get_height()
    label = f'{height}' if height != 0 else '> 3600s'  # Ajuste para mostrar '> 3600s' quando for 0
    ax2.text(bar.get_x() + bar.get_width() / 2.0, height, label, ha='center', va='bottom', fontsize=12, color='black')

for i, bar in enumerate(ax2.bar([i + 0.25 for i in x2], df_new["Incremental (s)"][3:], width=0.25)):
    height = bar.get_height()
    label = f'{height}' if height != 0 else '> 3600s'  # Ajuste para mostrar '> 3600s' quando for 0
    ax2.text(bar.get_x() + bar.get_width() / 2.0, height, label, ha='center', va='bottom', fontsize=12, color='black')

for i, bar in enumerate(ax2.bar([i + 0.5 for i in x2], df_new["Incremental + Length (s)"][3:], width=0.25)):
    height = bar.get_height()
    label = f'{height}' if height != 0 else '> 3600s'  # Ajuste para mostrar '> 3600s' quando for 0
    ax2.text(bar.get_x() + bar.get_width() / 2.0, height, label, ha='center', va='bottom', fontsize=12, color='black')

# Ajustando o layout e exibindo o gráfico
plt.tight_layout()
plt.show()
