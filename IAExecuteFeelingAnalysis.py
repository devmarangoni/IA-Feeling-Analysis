import os
import joblib
import IACheckDependencies
import IATrainingModel
import IAFeelingAnalysis

def checkDependencies():
    print("✅ Verificando dependências...\n")
    IACheckDependencies.check()

def trainModel():
    print("\n🧠 Inicializando treinamento da IA de Análise Sentimental...\n")
    IATrainingModel.train()

def executeSentimentAnalysis():
    print("\n🚀 Executando a análise de sentimentos agora!\n")
    IAFeelingAnalysis.main()

if __name__ == "__main__":
    checkDependencies()
    trainModel()
    executeSentimentAnalysis()
