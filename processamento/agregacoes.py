import pandas as pd

def agregar_duracao(df):
    agrupado = df.groupby(['Assunto', 'Categorias'], as_index=False)['Duração (horas)'].sum()
    agrupado = agrupado.sort_values(by='Categorias')
    return agrupado


def contar_eventos_por_data(df, coluna_data):
    df[coluna_data] = pd.to_datetime(df[coluna_data], errors="coerce")
    resultado = df[coluna_data].value_counts().sort_index()
    resultado.name = coluna_data  # alinhado com o nome da coluna original
    return resultado
