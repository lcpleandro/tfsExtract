def preparar_saida(df):
    df['Work Item Type'] = 'Task'
    df['Tags'] = df['Categorias'].str.split(' - ').str[0]
    df = df.rename(columns={
        'Assunto': 'Title',
        'Duração (horas)': 'Original Estimate'
    })
    df = df[['Work Item Type', 'Title', 'Tags', 'Original Estimate']]
    df = df[(df['Tags'] != '') & (df['Tags'] != 'Cancelado;GCOE')]
    return df
