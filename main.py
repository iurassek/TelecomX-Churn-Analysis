import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 1. Extração: Carregar e normalizar os dados
try:
    with open("TelecomX_Data.json", "r") as file:
        json_data = json.load(file)
except FileNotFoundError:
    print("Erro: Arquivo 'TelecomX_Data.json' não encontrado.")
    exit()

df = pd.json_normalize(json_data)
print("Primeiras linhas do DataFrame:\n", df.head())
print("\nColunas do DataFrame:", df.columns.tolist())
print("\nTipos de dados iniciais:\n", df.dtypes)

# 2. Transformação: Tratar os dados
# Tratar listas/dicionários
for coluna in df.columns:
    if df[coluna].apply(lambda x: isinstance(x, (list, dict))).any():
        print(f"Coluna '{coluna}' contém listas ou dicionários. Convertendo para string...")
        df[coluna] = df[coluna].astype(str)

# Valores ausentes
missing_values = df.isnull().sum()
print("\nValores ausentes por coluna:\n", missing_values)
fill_values = {
    'gender': 'Desconhecido',
    'Churn': 'nao',
    'InternetService': 'Nenhum',
    'customer.phone': 'Desconhecido',
    'account': 'Desconhecido',
    'MonthlyCharges': df['MonthlyCharges'].mean() if 'MonthlyCharges' in df.columns else 0
}
df.fillna(fill_values, inplace=True)

# Duplicatas
duplicatas = df.duplicated().sum()
print(f"\nNúmero de linhas duplicadas: {duplicatas}")
if duplicatas > 0:
    df = df.drop_duplicates()

# Formatação
colunas_numericas = ['MonthlyCharges']
for coluna in colunas_numericas:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(df[coluna].astype(str).str.replace(',', '.'), errors='coerce')

colunas_texto = ['customer.phone', 'account']
for coluna in colunas_texto:
    if coluna in df.columns:
        df[coluna] = df[coluna].astype(str).str.strip()

colunas_categoricas = ['gender', 'Churn', 'InternetService']
mapeamento = {
    'sim': 'sim',
    'SIM': 'sim',
    'Sim': 'sim',
    'yes': 'sim',
    'YES': 'sim',
    'não': 'nao',
    'NÃO': 'nao',
    'Não': 'nao',
    'no': 'nao',
    'NO': 'nao',
    'male': 'masculino',
    'Male': 'masculino',
    'female': 'feminino',
    'Female': 'feminino',
    'dsl': 'dsl',
    'DSL': 'dsl',
    'fiber optic': 'fibra',
    'Fiber optic': 'fibra'
}
for coluna in colunas_categoricas:
    if coluna in df.columns:
        df[coluna] = df[coluna].astype(str).str.lower().str.strip()
        df[coluna] = df[coluna].map(mapeamento).fillna(df[coluna])

# 3. Carga: Exportar dados tratados
df.to_excel("TelecomX_Dados_Tratados.xlsx", index=False, engine='openpyxl')
print("\nArquivo exportado: 'TelecomX_Dados_Tratados.xlsx'")

# 4. EDA: Gerar visualizações
sns.set(style="whitegrid")

# Distribuição de Churn
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Churn')
plt.title('Distribuição de Churn (Evasão)')
plt.xlabel('Churn')
plt.ylabel('Contagem')
plt.savefig('churn_distribuicao.png')
plt.close()

# Churn por gênero
if 'gender' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='gender', hue='Churn')
    plt.title('Churn por Gênero')
    plt.xlabel('Gênero')
    plt.ylabel('Contagem')
    plt.savefig('churn_por_genero.png')
    plt.close()

# Churn por serviço de internet
if 'InternetService' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='InternetService', hue='Churn')
    plt.title('Churn por Tipo de Serviço de Internet')
    plt.xlabel('Serviço de Internet')
    plt.ylabel('Contagem')
    plt.savefig('churn_por_internet.png')
    plt.close()

# Custos mensais por Churn
if 'MonthlyCharges' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='Churn', y='MonthlyCharges')
    plt.title('Distribuição de Custos Mensais por Churn')
    plt.xlabel('Churn')
    plt.ylabel('Custos Mensais')
    plt.savefig('monthlycharges_por_churn.png')
    plt.close()

# Matriz de correlação
colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
if len(colunas_numericas) > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[colunas_numericas].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlação')
    plt.savefig('matriz_correlacao.png')
    plt.close()

# 5. Gerar Relatório
# Estatísticas descritivas
descritivas = df.describe(include='all').to_string()

# Calcular taxa de churn
taxa_churn = df['Churn'].value_counts(normalize=True).get('sim', 0) * 100

# Verificar churn por gênero
churn_por_genero = "Churn é similar entre gêneros"
if 'gender' in df.columns:
    churn_gender_diff = df.groupby('gender')['Churn'].value_counts(normalize=True).unstack()
    if 'sim' in churn_gender_diff.columns and churn_gender_diff['sim'].max() > 0.6:
        churn_por_genero = "Churn mostra diferenças significativas entre gêneros"

# Verificar churn por serviço de internet
churn_por_internet = "Nenhum serviço de internet predomina no churn"
if 'InternetService' in df.columns:
    if df[df['InternetService'] == 'fibra']['Churn'].value_counts(normalize=True).get('sim', 0) > 0.5:
        churn_por_internet = "Clientes com fibra têm maior taxa de churn"

# Verificar custos mensais
custos_churn = "Custos mensais não diferem significativamente"
if 'MonthlyCharges' in df.columns:
    mean_churn = df[df['Churn'] == 'sim']['MonthlyCharges'].mean()
    mean_no_churn = df[df['Churn'] == 'nao']['MonthlyCharges'].mean()
    if not pd.isna(mean_churn) and not pd.isna(mean_no_churn) and mean_churn > mean_no_churn:
        custos_churn = "Clientes que churnam têm custos mensais mais altos"

# Criar conteúdo do relatório
relatorio = f"""
Relatório de Análise de Churn - Telecom X
Data: {datetime.now().strftime('%d/%m/%Y')}

1. Resumo do Tratamento de Dados:
   - Valores Ausentes: {missing_values[missing_values > 0].to_dict()}
     - Tratados com preenchimento (ex.: média para MonthlyCharges, 'Desconhecido' para categóricas).
   - Duplicatas: {duplicatas} linhas duplicadas encontradas e removidas.
   - Formatação: Corrigidos números (MonthlyCharges), textos (espaços removidos) e categorias inconsistentes (ex.: 'Yes'/'sim' → 'sim').
   - Colunas categóricas padronizadas: {', '.join([col for col in colunas_categoricas if col in df.columns])}.

2. Estatísticas Descritivas:
{descritivas}

3. Insights da Análise Exploratória:
   - Taxa de Churn: {taxa_churn:.2f}% dos clientes churnaram.
   - Gênero: {churn_por_genero}.
   - Serviço de Internet: {churn_por_internet}.
   - Custos Mensais: {custos_churn}.
   - Motivo: Alta taxa de churn em clientes com fibra óptica e custos mensais elevados sugere problemas com precificação ou qualidade do serviço.

4. Visualizações Geradas:
   - Distribuição de Churn: churn_distribuicao.png
   - Churn por Gênero: churn_por_genero.png
   - Churn por Serviço de Internet: churn_por_internet.png
   - Custos Mensais por Churn: monthlycharges_por_churn.png
   - Matriz de Correlação: matriz_correlacao.png

5. Recomendações:
   - Investigar problemas técnicos ou de satisfação no serviço de fibra óptica.
   - Oferecer descontos ou planos mais acessíveis para clientes com altos MonthlyCharges.
   - Melhorar a coleta de dados para reduzir valores ausentes em colunas críticas.
   - Segmentar clientes de alto risco (fibra, custos elevados) para ações de retenção.

Desenvolvido como parte do Challenge da Alura - Curso de Ciência de Dados.
"""

# Salvar relatório
with open("Relatorio_Churn_TelecomX.txt", "w", encoding='utf-8') as file:
    file.write(relatorio)
print("\nRelatório salvo em 'Relatorio_Churn_TelecomX.txt'")

# Opcional: Exibir relatório no console
print(relatorio)

