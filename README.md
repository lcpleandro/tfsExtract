#  Diagnóstico de Dados de Processos (Sprint)

Este projeto tem como objetivo fornecer um pipeline leve e interpretável para diagnóstico de dados operacionais oriundos de diferentes sprints de levantamento. Ele ajuda a identificar ruídos, padrões e possíveis distorções nos dados antes de qualquer modelagem ou visualização.

---

##  Funcionalidades principais

###  Pré-processamento (módulo `processamento/`)
- `filtrar_categorias_irrelevantes`: remove rótulos genéricos como `'almoço'`, `'_others'` ou outros termos operacionais que distorcem análises.
- `contar_eventos_por_data`: gera contagens cronológicas para análises de volume por período.
- (Em desenvolvimento) Funções adicionais de agrupamento, tratamento de colunas nulas, detecção de colunas constantes.

###  Testes unitários (`tests/`)
- Cada função é validada com dados simulados, sem hardcode de colunas.
- Testes cobrem tanto o comportamento esperado quanto edge cases.
- Usamos `pytest` + `pandas.testing` para validação precisa de estruturas.

---

##  Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/lcpleandro/tfsExtract.git
cd sprint_processos
