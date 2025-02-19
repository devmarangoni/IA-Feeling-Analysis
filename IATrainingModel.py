import nltk
import random
import joblib
import os
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from deep_translator import GoogleTranslator

nltk.download("movie_reviews")

MODEL_DIR = "ModelTraining"
MODEL_PATH = os.path.join(MODEL_DIR, "feelingModel.pkl")
USER_FEEDBACK_PATH = os.path.join(MODEL_DIR, "userFeedbackModel.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

def loadUserFeedback():
    if os.path.exists(USER_FEEDBACK_PATH):
        return joblib.load(USER_FEEDBACK_PATH)
    return []

def saveUserFeedback(feedback_data):
    joblib.dump(feedback_data, USER_FEEDBACK_PATH)

def train():
    if os.path.exists(MODEL_PATH):
        print("✅ Modelo de IA já treinado. Pulando treinamento.")
        return

    feelingTrainingData = []
    for category in movie_reviews.categories():
        for file in movie_reviews.fileids(category):
            words = movie_reviews.words(file)
            text = " ".join(words)
            feelingTrainingData.append((text, category))
    
    userFeedback = loadUserFeedback()
    feelingTrainingData.extend(userFeedback)
    
    random.shuffle(feelingTrainingData)

    texts, labels = zip(*feelingTrainingData)

    vectorizer = TfidfVectorizer()
    XTrain = vectorizer.fit_transform(texts)
    classifier = MultinomialNB()
    classifier.fit(XTrain, labels)

    joblib.dump((vectorizer, classifier), MODEL_PATH)
    print("✅ Modelo de IA treinado e salvo com sucesso em 'ModelTraining/'.")

def retrainModel(text, label):
    translated_text = GoogleTranslator(source='pt', target='en').translate(text)
    
    userFeedback = loadUserFeedback()
    userFeedback.append((translated_text, label))
    saveUserFeedback(userFeedback)
    
    vectorizer, classifier = joblib.load(MODEL_PATH)
    XNew = vectorizer.transform([translated_text])
    classifier.partial_fit(XNew, [label], classes=["pos", "neg"])
    
    joblib.dump((vectorizer, classifier), MODEL_PATH)
    print("✅ IA atualizada e feedback salvo em 'userFeedbackModel.pkl'.")