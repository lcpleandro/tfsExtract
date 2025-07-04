import pandas as pd
from .io_utils import carregar_csv, remover_virgulas_title
from .filtros import filtrar_categorias, filtrar_tags_por_tipo
from .transformacoes import converter_colunas_de_tempo, combinar_data_hora, calcular_duracao
from .limpeza import remover_colunas_irrelevantes
from .agregacoes import agregar_duracao
from .saida import preparar_saida

# ================================
# FUNÇÃO: extrair_sprint_formatada
# Extrai a informação da sprint a partir do caminho do arquivo (ex: '2025.w27')
# e converte para o formato padronizado '2025 W27', utilizado em identificadores e diretórios.
# ================================
def extrair_sprint_formatada(caminho):
    import os
    partes = caminho.lower().split(os.sep)
    for parte in partes:
        if 'w' in parte:
            return parte.replace('.', ' ').upper()
    return 'SAIDA'

# ================================
# FUNÇÃO: processar_csv_sprint
# Orquestra todas as etapas de processamento e aplica filtros conforme o tipo de arquivo.
# ================================
def processar_csv_sprint(caminho_arquivo, tipo_arquivo=None):
    df = carregar_csv(caminho_arquivo)
    df = remover_virgulas_title(df)
    df = filtrar_categorias(df)
    df = converter_colunas_de_tempo(df)
    df = combinar_data_hora(df)
    df = calcular_duracao(df)
    df = remover_colunas_irrelevantes(df)
    df = agregar_duracao(df)
    df = preparar_saida(df)
    df = filtrar_tags_por_tipo(df, tipo_arquivo)
    return df
