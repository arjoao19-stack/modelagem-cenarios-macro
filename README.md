# 📊 Modelagem de Cenários Macroeconômicos Futuros (Brasil 2026-2027)

Este projeto utiliza Python para construir modelos preditivos e análises de múltiplos cenários para o comportamento futuro da inflação (IPCA) e do mercado de ações (Índice Bovespa), cobrindo o horizonte macroeconômico até dezembro de 2027.

## 🛠️ Tecnologias Utilizadas
- **Python 3** como linguagem base.
- **Pandas**: Estruturação de dataframes e séries preditivas.
- **Numpy**: Processamento matemático e funções lineares de tendência.
- **Matplotlib**: Modelagem de painéis visuais multi-gráficos.

## 📈 Modelagem de Cenários (Premissas baseadas no Relatório Focus)
O script gera um painel duplo simulando duas narrativas de mercado pós-eleitorais:
1. **Cenário Base (Mercado):** Convergência gradual do IPCA rumo à meta e recuperação estrutural do Ibovespa.
2. **Cenário de Estresse (Risco):** Pressão inflacionária persistente devido ao risco fiscal, impactando diretamente o valuation das empresas na B3.

## 🚀 Como Executar o Projeto
1. Instale as bibliotecas necessárias:
```bash
pip install pandas matplotlib numpy
```
2. Execute o arquivo preditivo:
```bash
python projeção_macro.py
```
