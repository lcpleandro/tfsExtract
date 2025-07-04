import pandas as pd

def converter_colunas_de_tempo(df):
    df['Data de início'] = pd.to_datetime(df['Data de início'], errors='coerce').dt.date
    df['Hora de início'] = pd.to_datetime(df['Hora de início'], format='%H:%M:%S', errors='coerce').dt.time
    df['Data de término'] = pd.to_datetime(df['Data de término'], errors='coerce').dt.date
    df['Hora de término'] = pd.to_datetime(df['Hora de término'], format='%H:%M:%S', errors='coerce').dt.time
    return df

def combinar_data_hora(df):
    df['DataHoraInicio'] = pd.to_datetime(df['Data de início'].astype(str) + ' ' + df['Hora de início'].astype(str), errors='coerce')
    df['DataHoraFim'] = pd.to_datetime(df['Data de término'].astype(str) + ' ' + df['Hora de término'].astype(str), errors='coerce')
    return df

def calcular_duracao(df):
    df['Duração (horas)'] = (df['DataHoraFim'] - df['DataHoraInicio']).dt.total_seconds() / 3600
    return df
