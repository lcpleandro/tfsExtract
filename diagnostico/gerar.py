# ================================
# FUNÇÃO: gerar_diagnostico
# Exibe uma prévia do DataFrame processado, tipos de colunas e estatísticas básicas.
# ================================
def gerar_diagnostico(df):
    print("\n📋 Prévia dos dados (top 10 linhas):")
    print(df.head(10))

    print("\n🔍 Colunas e tipos:")
    print(df.dtypes)

    print("\n📊 Estatísticas básicas:")
    print(df.describe())
