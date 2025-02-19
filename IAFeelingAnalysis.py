import os
from deep_translator import GoogleTranslator
import joblib
import IATrainingModel

MODEL_DIR = "ModelTraining"
MODEL_PATH = os.path.join(MODEL_DIR, "feelingModel.pkl")

def feelingPredict(text):
    if not os.path.exists(MODEL_PATH):
        print("⚠️ O modelo não foi encontrado! Execute o treinamento primeiro.")
        return "ERRO: MODELO NÃO ENCONTRADO", None

    vectorizer, classifier = joblib.load(MODEL_PATH)

    translatedText = GoogleTranslator(source='pt', target='en').translate(text)
    
    XInput = vectorizer.transform([translatedText])
    result = classifier.predict(XInput)[0]
    
    FEELING_LABELS = {
        "pos": "FRASE POSITIVA",
        "neg": "FRASE NEGATIVA"
    }
    
    return FEELING_LABELS.get(result, "FRASE NEUTRA"), result

def main():
    print("🧐 Digite frases para analisar o sentimento (ou 'sair' para encerrar)")

    while True:
        userInput = input("\nDigite uma frase para análise de sentimento: ")
        if userInput.strip().lower() == "sair":
            print("🚪 Encerrando o programa...")
            break
        
        feeling, rawResult = feelingPredict(userInput)
        
        if rawResult is None:
            continue  # Se o modelo não foi encontrado, evita erro e pede outra entrada
        
        print(f"💬 Sentimento detectado: {feeling}")
        
        feedback = input("🤔 Concorda com a análise? (s/n): ").strip().lower()
        if feedback == "n":
            correctLabel = "neg" if rawResult == "pos" else "pos"
            IATrainingModel.retrainModel(userInput, correctLabel)
            print(f"🔄 Ajustado automaticamente para: {correctLabel.upper()}")
            