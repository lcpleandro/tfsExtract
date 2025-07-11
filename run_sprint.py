import csv
from processamento.pipeline import processar_csv_sprint, extrair_sprint_formatada
from diagnostico.gerar import gerar_diagnostico
import os

if __name__ == "__main__":
    # =========================================
    # 1. Caminho do arquivo CSV a ser processado
    # =========================================
    caminho_arquivo = r'C:\Users\Leandro\OneDrive - ArcelorMittal\Desktop\hist_sprint\2025.w29\2025.W29 - plan.CSV'

    # =========================================
    # 2. Processa e diagnostica o tipo de Input - nplan ou plan
    # =========================================
    nome_arquivo_origem = os.path.basename(caminho_arquivo).lower()
    tipo = 'nplan' if 'nplan' in nome_arquivo_origem else ('plan' if 'plan' in nome_arquivo_origem else 'saida')

    df = processar_csv_sprint(caminho_arquivo, tipo_arquivo=tipo)
    
    gerar_diagnostico(df)

    # =========================================
    # 3. Geração do nome de saída - pasta e arquivo
    # =========================================
    sprint_formatada = extrair_sprint_formatada(caminho_arquivo)
    sprint_raw = sprint_formatada.replace(' ', '.').lower()

    nome_original = os.path.basename(caminho_arquivo)
    nome_base, extensao = os.path.splitext(nome_original)

    nome_final = f'{nome_base} - tfs_format{extensao}'
    caminho_final = os.path.join(os.path.dirname(caminho_arquivo), nome_final)

    # =========================================
    # 3.1 Adiciona colunas de Iteration e Area Path
    # =========================================
    iteration_path = f'LCB-TI\\LCB-TI-COE Analytics\\{sprint_formatada}'
    area_path = 'LCB-TI\\LCB-TI-COE Analytics'
    df['Iteration Path'] = iteration_path
    df['Area Path'] = area_path
    df['Assigned To'] = "<leandro.pacheco1@arcelormittal.com.br>"

    # =========================================
    # 4. Confirmação e salvamento
    # =========================================
    resposta = input(f"\nDeseja salvar os dados em '{caminho_final}'? (s/n): ").strip().lower()
    if resposta == 's':
        df.to_csv(caminho_final, index=False, sep=',', float_format='%.2f', encoding='utf-8',quoting=csv.QUOTE_NONNUMERIC)
        print(f"\n✅ Arquivo salvo com sucesso em:\n{caminho_final}")
    else:
        print("\n❌ Salvamento cancelado.")
