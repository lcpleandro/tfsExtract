import pandas as pd

# ================================
# FUNÇÃO: carregar_csv
# Lê o arquivo CSV a partir do caminho indicado e retorna um DataFrame do pandas.
# ================================
def carregar_csv(caminho_arquivo):
    return pd.read_csv(caminho_arquivo, encoding='utf-8')

# ================================
# FUNÇÃO: remover_virgulas_title
# Remove vírgulas da coluna de títulos (por padrão 'Title') para evitar quebra no CSV.
# ================================
def remover_virgulas_title(df, coluna='Title'):
    if coluna in df.columns:
        df[coluna] = df[coluna].astype(str).str.replace(',', ' ', regex=False)
    else:
        print(f"⚠️ Coluna '{coluna}' não encontrada. Nenhuma vírgula removida.")
    return df
