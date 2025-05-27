# TelecomX - Análise de Evasão de Clientes

## Descrição do Projeto
Este é o **Challenge Análise de Evasão TelecomX - Alura** do curso de Ciência de Dados. O objetivo é realizar uma análise das informações para a **TelecomX**, uma empresa que enfrenta altos índices de cancelamentos. A análise visa identificar fatores que contribuem para a perda de clientes, fornecendo insights para a equipe de Data Science desenvolver modelos preditivos e estratégias de retenção.

### Desafio
Eu fui contratado como assistente de análise de dados na TelecomX para o projeto "Churn de Clientes". O desafio envolve:
- **Coletar e tratar dados** de um arquivo JSON.
- **Aplicar o processo ETL** (Extração, Transformação, Carga) para preparar os dados.
- **Realizar uma Análise Exploratória de Dados (EDA)** com visualizações para identificar padrões.
- **Gerar um relatório** com insights relevantes para reduzir a evasão.

### Objetivos Praticados
- ✅ Importar e manipular dados de uma API ou arquivo JSON de forma eficiente.
- ✅ Aplicar conceitos de ETL na preparação dos dados.
- ✅ Criar visualizações estratégicas para identificar padrões e tendências.
- ✅ Realizar EDA e gerar um relatório com insights.

## Análises Realizadas
Os dados foram extraídos do arquivo `TelecomX_Data.json` e normalizados em um formato tabular usando `pd.json_normalize`. As seguintes verificações e tratamentos foram realizados:
1. **Valores Ausentes**: Identificados com `df.isnull().sum()` e tratados com preenchimento (ex.: média para `MonthlyCharges`, "Desconhecido" para categóricas).
2. **Dados Duplicados**: Verificados com `df.duplicated()` e removidos, se necessário.
3. **Erros de Formatação**: Corrigidos números (ex.: `MonthlyCharges` para float), datas (ex.: `tenure`, se aplicável) e textos (ex.: remoção de espaços).
4. **Categorias Inconsistentes**: Padronizadas (ex.: "Sim"/"Yes" → "sim", "Male"/"male" → "masculino") usando mapeamento.

### Visualizações Geradas
Foram criados gráficos com `matplotlib` e `seaborn` para explorar a evasão:
- **Distribuição de Evasão**: Gráfico de contagem (`countplot`) mostrando a proporção de clientes que evadiram (`sim`) versus não evadiram (`nao`).
- **Evasão por Gênero**: Gráfico de contagem por `genero` com `matriz='Evasão'`.
- **Evasão por Serviço de Internet**: Gráfico de contagem por `InternetService` com `matriz='Evasão'`.
- **Custos Mensais por Evasão**: Boxplot comparando `MonthlyCharges` entre clientes com e sem evasão.
- **Matriz de Correlação**: Heatmap para variáveis numéricas, mostrando relações (ex.: entre `MonthlyCharges` e outras variáveis).

Os gráficos foram salvos como `churn_distribuicao.png`, `churn_por_genero.png`, `churn_por_internet.png`, `monthlycharges_por_churn.png` e `matriz_correlacao.png`.

## Resultados Encontrados
- **Taxa de Evasão**: Aproximadamente `25.72%` dos clientes evadiram.
- **Gênero**: O evasão é similar entre gêneros, sugerindo que `genero` não é um fator determinante.
- **Serviço de Internet**: Clientes com serviço de fibra óptica (`fibra`) apresentam maior taxa de evasão, possivelmente devido a custos ou qualidade do serviço.
- **Custos Mensais**: Clientes que evadiram tendem a ter `MonthlyCharges` mais altos, indicando que o preço pode ser um fator de evasão.
- **Motivo**: A alta taxa de evasão entre clientes com fibra e custos elevados sugere problemas com precificação ou satisfação com o serviço de internet.

## Recomendações
1. **Investigar o Serviço de Fibra**: Analisar reclamações ou problemas técnicos associados ao serviço de fibra óptica, que apresenta maior evasão.
2. **Revisar Precificação**: Oferecer descontos ou planos mais acessíveis para clientes com altos `MonthlyCharges`, especialmente aqueles com fibra.
3. **Melhorar Coleta de Dados**: Reduzir valores ausentes em colunas críticas (ex.: `MonthlyCharges`) para análises mais precisas.
4. **Segmentação de Clientes**: Priorizar estratégias de retenção para clientes com características de alto risco de evasão (ex.: fibra, custos elevados).

## Como Executar
1. **Pré-requisitos**:
   ```bash
   pip install pandas numpy requests matplotlib seaborn openpyxl# Telecom X - Análise de Evasão de Clientes
