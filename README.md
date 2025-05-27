# 🧠 Projeto de Detecção de Fraudes com Machine Learning

Este projeto tem como objetivo construir um sistema completo de **detecção de fraudes em transações financeiras**, desde a geração dos dados até a aplicação prática via **aplicativo iOS**, utilizando:

- 🐍 **Python** (para modelagem e pré-processamento)
- 🧪 **Scikit-learn** (modelos: Random Forest e Regressão Logística)
- 💾 **Create ML** (para exportar o modelo como `.mlmodel`)
- 📱 **SwiftUI** (app iOS com MVVM + CoreML)

---

## 🗂️ Estrutura do Projeto

```
Fraud-Predictor/
├── data/
│   └── transacoes_fraude_sujo.csv          # Dataset com dados sintéticos
│   ├── fraude_teste.csv                    # Dataset com dados de teste para CreateML
│   └── fraude_treino.csv                   # Dataset com dados de treino para CreateML
├── notebooks/
│   └── analisys-preproc.ipynb              # Pré-processamento e modelagem
├── models/
│   ├── modelo_fraude.pkl                   # Modelo RandomForest treinado (joblib)
│   ├── FraudPredcitor.mlproj
│   └── ModeloFraude.mlmodel                # Modelo exportado via CreateML
├── scripts/
│   ├── create-sintetic-csv.py              # Gera CSV com dados nulos e inválidos
│   ├── testing.py                          # Faz previsões com modelo treinado
│   └── exporting-coreml.py                 # Gera CSVs de treino e teste para CreateML
├── app-ios/
│   └── FraudPredictor.swift                # App iOS com SwiftUI + CoreML
└── README.md
```

---

## 📊 Etapas do Projeto

### 1. Geração de Dados Sintéticos

O script `gerar_dados.py` cria um dataset simulado de transações financeiras, incluindo:

- Inserção de valores nulos e inconsistentes propositalmente
- Simulação de desbalanceamento nas classes (fraudes x legítimas)

### 2. Análise e Pré-processamento (Python Notebook)

No notebook `analise_modelagem.ipynb`, realizamos:

- Análise exploratória (histogramas, boxplots, correlação)
- Tratamento de nulos com mediana
- Verificação de consistência de variáveis categóricas e binárias
- Normalização e separação entre treino e teste

### 3. Modelagem (Random Forest e Regressão Logística)

Foram treinados dois modelos:

- ✅ **Random Forest**: boa acurácia e robusto a outliers
- 🧮 **Regressão Logística**: modelo mais interpretável

A avaliação dos modelos considerou:

- Matriz de Confusão
- Acurácia, Precisão, Recall, F1-Score
- **ROC-AUC**

### 4. Exportação e Inferência

- O modelo RandomForest foi salvo com `joblib`
- Um script (`testar_modelo.py`) permite realizar previsões localmente
- Também criamos um CSV de treino/teste compatível com o **Create ML**

---

## 🧠 Treinamento com Create ML

Usamos o template **Tabular Classification** no CreateML, carregando os dados tratados do Python, para gerar o arquivo `.mlmodel` utilizado no app iOS.

---

## 📱 Aplicativo iOS com CoreML

O app iOS foi desenvolvido em:

- **Swift 6**
- **SwiftUI**
- Arquitetura **MVVM**
- Integração com **CoreML**

O app realiza a previsão local usando o modelo `ModeloFraude.mlmodel`.

### Como usar:

1. Clonar o projeto e abrir em Xcode
2. Certificar-se que `ModeloFraude.mlmodel` está no bundle
3. Executar no simulador ou em dispositivo real

---

## 🚀 Requisitos

### Python

- Python 3.10+
- pandas, numpy, seaborn, matplotlib, scikit-learn, joblib

### iOS

- Xcode 15+
- Swift 6
- iOS 16.0+

---

