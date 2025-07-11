# ================================
# FUNÇÃO: gerar_diagnostico
# Exibe uma prévia do DataFrame processado, tipos de colunas e estatísticas básicas.
# ================================
def gerar_diagnostico(df):
    print("\n🧪 Diagnóstico rápido do dataframe:")
    print(f"\n📊 Total de linhas: {len(df)}")
    print(f"📋 Colunas: {list(df.columns)}")
    print(f"Soma de Original Estimate: {df['Original Estimate'].sum()}")
    print(f"head 5 do dataframe:")
    print(df.head(5))
    print("\n🧪 Fim do Diagnóstico rápido do dataframe:")
