import pandas as pd
from processamento.filtros import filtrar_categorias_irrelevantes

# ===========================================================
# TESTE UNITÁRIO: test_filtrar_categorias_irrelevantes
# Verifica se a função remove corretamente as categorias consideradas irrelevantes
# para análise, com base em uma lista de termos indesejados.
# ===========================================================
def test_filtrar_categorias_irrelevantes():
    # Cria um DataFrame de exemplo com categorias diversas, incluindo irrelevantes
    df = pd.DataFrame({'categoria': ['almoço', 'nplan_logistica', '_others', 'energia']})
    
    # Define os termos que devem ser removidos do DataFrame
    termos = ['almoço', '_others']
    
    # Executa a função real a ser testada
    resultado = filtrar_categorias_irrelevantes(df, 'categoria', termos)
    
    # Verifica se a saída contém apenas as categorias relevantes
    assert resultado['categoria'].tolist() == ['nplan_logistica', 'energia']
