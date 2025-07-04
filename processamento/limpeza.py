def remover_colunas_irrelevantes(df):
    colunas_para_remover = [
        "Data de início", "Hora de início", "Data de término", "Hora de término", "O dia inteiro", 
        "Lembrete ativado/desativado", "Data do lembrete", "Horário do lembrete", "Organizador da reunião", 
        "Participantes necessários", "Participantes opcionais", "Recursos da reunião", "Descrição", 
        "Informações para cobrança", "Local", "Mostrar horário como", "Particular", "Prioridade", 
        "Quilometragem", "Sensibilidade"
    ]
    return df.drop(columns=[col for col in colunas_para_remover if col in df.columns])
