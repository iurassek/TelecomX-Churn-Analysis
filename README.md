# TelecomX-Churn-Analysis
# Telecom X - Análise de Evasão de Clientes

## Descrição do Projeto
Este projeto é parte do **Challenge da Alura** no curso de Ciência de Dados. O objetivo é realizar uma análise de evasão de clientes (churn) para a **Telecom X**, uma empresa que enfrenta altos índices de cancelamentos. A análise visa identificar fatores que contribuem para a perda de clientes, fornecendo insights para a equipe de Data Science desenvolver modelos preditivos e estratégias de retenção.

### Desafio
Você foi contratado como assistente de análise de dados na Telecom X para o projeto "Churn de Clientes". O desafio envolve:
- **Coletar e tratar dados** de um arquivo JSON (ou API, se disponível).
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
Foram criados gráficos com `matplotlib` e `seaborn` para explorar o churn:
- **Distribuição de Churn**: Gráfico de contagem (`countplot`) mostrando a proporção de clientes que churnaram (`sim`) versus não churnaram (`nao`).
- **Churn por Gênero**: Gráfico de contagem por `gender` com `hue='Churn'`.
- **Churn por Serviço de Internet**: Gráfico de contagem por `InternetService` com `hue='Churn'`.
- **Custos Mensais por Churn**: Boxplot comparando `MonthlyCharges` entre clientes com e sem churn.
- **Matriz de Correlação**: Heatmap para variáveis numéricas, mostrando relações (ex.: entre `MonthlyCharges` e outras variáveis).

Os gráficos foram salvos como `churn_distribuicao.png`, `churn_por_genero.png`, `churn_por_internet.png`, `monthlycharges_por_churn.png` e `matriz_correlacao.png`.

## Resultados Encontrados
- **Taxa de Churn**: Aproximadamente `{df['Churn'].value_counts(normalize=True)['sim']:.2%}` dos clientes churnaram (valor exato depende dos dados).
- **Gênero**: O churn é similar entre gêneros, sugerindo que `gender` não é um fator determinante.
- **Serviço de Internet**: Clientes com serviço de fibra óptica (`fibra`) apresentam maior taxa de churn, possivelmente devido a custos ou qualidade do serviço.
- **Custos Mensais**: Clientes que churnam tendem a ter `MonthlyCharges` mais altos, indicando que o preço pode ser um fator de evasão.
- **Motivo**: A alta taxa de churn entre clientes com fibra e custos elevados sugere problemas com precificação ou satisfação com o serviço de internet.

## Recomendações
1. **Investigar o Serviço de Fibra**: Analisar reclamações ou problemas técnicos associados ao serviço de fibra óptica, que apresenta maior churn.
2. **Revisar Precificação**: Oferecer descontos ou planos mais acessíveis para clientes com altos `MonthlyCharges`, especialmente aqueles com fibra.
3. **Melhorar Coleta de Dados**: Reduzir valores ausentes em colunas críticas (ex.: `MonthlyCharges`) para análises mais precisas.
4. **Segmentação de Clientes**: Priorizar estratégias de retenção para clientes com características de alto risco de churn (ex.: fibra, custos elevados).

## Como Executar
1. **Pré-requisitos**:
   ```bash
   pip install pandas numpy requests matplotlib seaborn openpyxl# Telecom X - Análise de Evasão de Clientes

## Descrição do Projeto
Este projeto é parte do **Challenge da Alura** no curso de Ciência de Dados. O objetivo é realizar uma análise de evasão de clientes (churn) para a **Telecom X**, uma empresa que enfrenta altos índices de cancelamentos. A análise visa identificar fatores que contribuem para a perda de clientes, fornecendo insights para a equipe de Data Science desenvolver modelos preditivos e estratégias de retenção.

### Desafio
Você foi contratado como assistente de análise de dados na Telecom X para o projeto "Churn de Clientes". O desafio envolve:
- **Coletar e tratar dados** de um arquivo JSON (ou API, se disponível).
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
Foram criados gráficos com `matplotlib` e `seaborn` para explorar o churn:
- **Distribuição de Churn**: Gráfico de contagem (`countplot`) mostrando a proporção de clientes que churnaram (`sim`) versus não churnaram (`nao`).
- **Churn por Gênero**: Gráfico de contagem por `gender` com `hue='Churn'`.
- **Churn por Serviço de Internet**: Gráfico de contagem por `InternetService` com `hue='Churn'`.
- **Custos Mensais por Churn**: Boxplot comparando `MonthlyCharges` entre clientes com e sem churn.
- **Matriz de Correlação**: Heatmap para variáveis numéricas, mostrando relações (ex.: entre `MonthlyCharges` e outras variáveis).

Os gráficos foram salvos como `churn_distribuicao.png`, `churn_por_genero.png`, `churn_por_internet.png`, `monthlycharges_por_churn.png` e `matriz_correlacao.png`.

## Resultados Encontrados
- **Taxa de Churn**: Aproximadamente `{df['Churn'].value_counts(normalize=True)['sim']:.2%}` dos clientes churnaram (valor exato depende dos dados).
- **Gênero**: O churn é similar entre gêneros, sugerindo que `gender` não é um fator determinante.
- **Serviço de Internet**: Clientes com serviço de fibra óptica (`fibra`) apresentam maior taxa de churn, possivelmente devido a custos ou qualidade do serviço.
- **Custos Mensais**: Clientes que churnam tendem a ter `MonthlyCharges` mais altos, indicando que o preço pode ser um fator de evasão.
- **Motivo**: A alta taxa de churn entre clientes com fibra e custos elevados sugere problemas com precificação ou satisfação com o serviço de internet.

## Recomendações
1. **Investigar o Serviço de Fibra**: Analisar reclamações ou problemas técnicos associados ao serviço de fibra óptica, que apresenta maior churn.
2. **Revisar Precificação**: Oferecer descontos ou planos mais acessíveis para clientes com altos `MonthlyCharges`, especialmente aqueles com fibra.
3. **Melhorar Coleta de Dados**: Reduzir valores ausentes em colunas críticas (ex.: `MonthlyCharges`) para análises mais precisas.
4. **Segmentação de Clientes**: Priorizar estratégias de retenção para clientes com características de alto risco de churn (ex.: fibra, custos elevados).

## Como Executar
1. **Pré-requisitos**:
   ```bash
   pip install pandas numpy requests matplotlib seaborn openpyxl
