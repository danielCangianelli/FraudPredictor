import pandas as pd
import numpy as np
import random
import os

np.random.seed(42)

num_total = 1000
fraude_percentual = 0.25
num_fraude = int(num_total * fraude_percentual)
num_legit = num_total - num_fraude

# Dados para transações legítimas
data_legit = {
    'id_transacao': range(1, num_legit + 1),
    'tempo_desde_ultima_transacao': np.random.randint(30, 3600, num_legit),
    'valor_transacao': np.random.lognormal(3, 1, num_legit) * 10,
    'localizacao_comerciante_risco': np.random.choice([0, 1], num_legit, p=[0.95, 0.05]),
    'frequencia_cartao_dia': np.random.randint(1, 15, num_legit),
    'media_gasto_cartao_semana': np.random.lognormal(4, 0.5, num_legit) * 50,
    'fraude': [0] * num_legit
}
df_legit = pd.DataFrame(data_legit)

# Dados para transações fraudulentas
data_fraude = {
    'id_transacao': range(num_legit + 1, num_total + 1),
    'tempo_desde_ultima_transacao': np.random.randint(1, 30, num_fraude),
    'valor_transacao': np.random.normal(2000, 500, num_fraude),
    'localizacao_comerciante_risco': np.random.choice([0, 1], num_fraude, p=[0.1, 0.9]),
    'frequencia_cartao_dia': np.random.randint(10, 50, num_fraude),
    'media_gasto_cartao_semana': np.random.normal(1000, 300, num_fraude),
    'fraude': [1] * num_fraude
}
df_fraude = pd.DataFrame(data_fraude)

# Concatenar e embaralhar
df = pd.concat([df_legit, df_fraude], ignore_index=True)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Inserir valores nulos propositalmente (5% aleatórios em algumas colunas)
for col in ['valor_transacao', 'tempo_desde_ultima_transacao', 'media_gasto_cartao_semana']:
    n = int(0.05 * len(df))
    indices = np.random.choice(df.index, n, replace=False)
    df.loc[indices, col] = np.nan

# Inserir valores "quebrados"
df.loc[random.randint(0, len(df)-1), 'frequencia_cartao_dia'] = -1  # valor inválido
df.loc[random.randint(0, len(df)-1), 'localizacao_comerciante_risco'] = 2  # fora do domínio [0,1]
df.loc[random.randint(0, len(df)-1), 'valor_transacao'] = 'erro'  # string no lugar de número

# Salvar CSV
output_filename = 'transacoes_fraude_sujo.csv'
output_directory = "data"
this_path = os.path.dirname(os.path.abspath(__file__))
project_path =  os.path.abspath(os.path.join(this_path, os.pardir))
output_path = os.path.join(project_path, output_directory, output_filename)

df.to_csv(output_path, index=False)
print(f"Arquivo '{output_filename}' gerado com sucesso no diretório: {os.getcwd()}")
