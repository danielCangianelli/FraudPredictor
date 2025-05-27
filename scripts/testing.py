import joblib
import pandas as pd

# 1. Carrega o modelo
modelo = joblib.load('./model/modelo_fraude.pkl')

# 2. Dados novos — deve ter as MESMAS colunas e pré-processamento
# nova_transacao = pd.DataFrame([{
#     'tempo_desde_ultima_transacao': 10,
#     'valor_transacao': 800,
#     'localizacao_comerciante_risco': 1,
#     'frequencia_cartao_dia': 12,
#     'media_gasto_cartao_semana': 450
# }])

# nova_transacao = pd.DataFrame([{
#     'tempo_desde_ultima_transacao': 1800,  # Muito maior
#     'valor_transacao': 200,
#     'localizacao_comerciante_risco': 0,
#     'frequencia_cartao_dia': 3,
#     'media_gasto_cartao_semana': 2000
# }])
nova_transacao = pd.DataFrame([{
    'tempo_desde_ultima_transacao': 100,  # Muito maior
    'valor_transacao': 500,
    'localizacao_comerciante_risco': 0,
    'frequencia_cartao_dia': 10,
    'media_gasto_cartao_semana': 2000
}])

# 3. Previsão
pred = modelo.predict(nova_transacao)

print("⚠️ Fraude detectada" if pred[0] == 1 else "✅ Transação legítima")
