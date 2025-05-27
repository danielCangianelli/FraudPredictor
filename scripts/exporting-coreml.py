import pandas as pd
import numpy as np
import os

this_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(this_path, os.pardir))
destination_path = "data"
file_name = "transacoes_fraude_sujo.csv" 

file_path = os.path.join(root_path, destination_path, file_name)
print(file_path)
df = pd.read_csv(file_path)
# Tentar forçar conversão para float e identificar erros
df['valor_transacao'] = pd.to_numeric(df['valor_transacao'], errors='coerce')
# Percentual de valores ausentes
df.isnull().mean().sort_values(ascending=False)
# Imputar valores ausentes com a mediana de cada coluna numérica
for col in ['tempo_desde_ultima_transacao', 'valor_transacao', 'media_gasto_cartao_semana', 'frequencia_cartao_dia']:
    mediana = df[col].median()
    df[col] = df[col].fillna(mediana)
    
# Corrigir valores inválidos para 0 (baixa suspeita)
df.loc[~df['localizacao_comerciante_risco'].isin([0, 1]), 'localizacao_comerciante_risco'] = 0

from sklearn.model_selection import train_test_split

# X: variáveis independentes, y: variável alvo
X = df.drop(columns=['id_transacao'])  # Se ainda não removido
y = df['fraude']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

df_train, df_test = train_test_split(df, test_size=0.2, random_state=42, stratify=df['fraude'])

train_file = os.path.join(root_path, destination_path, 'fraude_treino.csv')
test_file = os.path.join(root_path, destination_path, 'fraude_teste.csv')
# Exporta para arquivos CSV (sem índice, no formato aceito pelo Create ML)
df_train.to_csv(train_file, index=False)
df_test.to_csv(test_file, index=False)
