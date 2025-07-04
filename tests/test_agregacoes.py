import pandas as pd
from pandas.testing import assert_series_equal
from processamento.agregacoes import contar_eventos_por_data

# ===============================================
# TESTE UNITÁRIO: test_contar_eventos_por_data
# Verifica se a função contar_eventos_por_data retorna corretamente 
# a contagem de registros por data, considerando datas válidas.
# ===============================================

def test_contar_eventos_por_data():
    df = pd.DataFrame({
        'data_evento': ['2024-01-01', '2024-01-01', '2024-01-02', None]
    })

    esperado = pd.Series(
        [2, 1],
        index=pd.Index(pd.to_datetime(['2024-01-01', '2024-01-02']), name='data_evento'),
        name='data_evento'
    )

    resultado = contar_eventos_por_data(df, 'data_evento')

    assert_series_equal(resultado, esperado)
