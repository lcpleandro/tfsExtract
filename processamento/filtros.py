import re

# ================================
# FUNÇÃO: filtrar_categorias
# Remove linhas cuja coluna "Categorias" contenha termos indesejados como "almoço" ou "_others".
# ================================
def filtrar_categorias(df, termos_excluidos=None):
    if termos_excluidos is None:
        termos_excluidos = ['almoço', '_others']
    padrao = '|'.join(map(re.escape, termos_excluidos))
    filtro = df['Categorias'].astype(str).str.contains(padrao, case=False, regex=True)
    print(f"🧹 Linhas removidas por categoria: {filtro.sum()}")
    return df[~filtro]

# ================================
# FUNÇÃO: filtrar_tags_por_tipo
# Filtra linhas com base no tipo do arquivo (nplan ou plan), usando a coluna 'Tags'.
# ================================
def filtrar_tags_por_tipo(df, tipo):
    if 'Tags' not in df.columns:
        return df
    if tipo == 'nplan':
        return df[df['Tags'].str.contains('nplan', case=False, na=False)]
    elif tipo == 'plan':
        return df[~df['Tags'].str.contains('nplan', case=False, na=False)]
    return df

# ================================
# FUNÇÃO: filtrar_categorias_irrelevantes
# Remove linhas de um DataFrame em que os valores da coluna especificada
# correspondem a categorias irrelevantes, como 'almoço' ou '_others'.
#
# Contexto: usada na etapa inicial do diagnóstico para limpar ruídos que 
# distorcem contagens, análises de distribuição ou agrupamentos.
# Essencial para garantir que categorias genéricas ou operacionais não
# contaminem a análise de padrões relevantes (ex: NPLANs).
#
# Parâmetros:
# - df: DataFrame de entrada
# - coluna: nome da coluna categórica a ser filtrada
# - termos_irrelevantes: lista de strings com os valores a serem excluídos
#
# Retorna:
# - DataFrame contendo apenas categorias consideradas relevantes.
# ================================
def filtrar_categorias_irrelevantes(df, coluna, termos_irrelevantes):
    return df[~df[coluna].str.lower().isin(termos_irrelevantes)]