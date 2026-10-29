import os
import sys

print("Validando dependências do ambiente...")
os.system(f'"{sys.executable}" -m pip install --upgrade pandas matplotlib numpy')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Definindo o horizonte de projeção (Outubro/2026 até Dezembro/2027)
datas = pd.date_range(start='2026-10-01', end='2027-12-01', freq='MS')

# 2. Inserindo as premissas do mercado (Relatório Focus/BTG Pactual pós-eleições)
# Trajetória projetada: IPCA saindo da pressão atual rumo à convergência de 2027
ipca_cenario_base = np.linspace(4.62, 4.30, len(datas))
ipca_cenario_estresse = np.linspace(4.62, 5.20, len(datas))

# Trajetória projetada para Bolsa: Recuperação gradual vs Estresse de juros longos
ibov_cenario_base = np.linspace(128000, 142000, len(datas))
ibov_cenario_estresse = np.linspace(128000, 110000, len(datas))

# Estruturando os Dados no DataFrame
df_projecao = pd.DataFrame(index=datas)
df_projecao['IPCA (Base)'] = ipca_cenario_base
df_projecao['IPCA (Estresse)'] = ipca_cenario_estresse
df_projecao['Ibovespa (Base)'] = ibov_cenario_base
df_projecao['Ibovespa (Estresse)'] = ibov_cenario_estresse

# 3. Construção do Painel Visual de Projeções (2 Gráficos Lado a Lado)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Gráfico 1: Projeções para a Inflação (IPCA)
ax1.plot(df_projecao.index, df_projecao['IPCA (Base)'], color='orange', linewidth=2.5, linestyle='--', label='Cenário Base (Focus: 4.30%)')
ax1.plot(df_projecao.index, df_projecao['IPCA (Estresse)'], color='red', linewidth=2, linestyle=':', label='Cenário de Estresse Fiscal')
ax1.set_title('Projeção e Tendência do IPCA (Até Fim de 2027)', fontsize=11, fontweight='bold')
ax1.set_ylabel('IPCA Acumulado 12M (%)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right')

# Gráfico 2: Projeções para o Índice Bovespa
ax2.plot(df_projecao.index, df_projecao['Ibovespa (Base)'], color='green', linewidth=2.5, linestyle='--', label='Cenário Base (Recuperação)')
ax2.plot(df_projecao.index, df_projecao['Ibovespa (Estresse)'], color='darkred', linewidth=2, linestyle=':', label='Cenário de Estresse (Juros Altos)')
ax2.set_title('Tendência de Longo Prazo do Ibovespa', fontsize=11, fontweight='bold')
ax2.set_ylabel('Pontuação do Índice')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='lower left')

# Customização Geral
plt.suptitle('Modelagem de Cenários Macroeconômicos Futuros (Brasil 2026-2027)', fontsize=13, fontweight='bold', y=0.98)
plt.tight_layout()

print("\n[Sucesso] Abrindo painel gráfico de tendências futuras...")
plt.show()
