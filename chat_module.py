import secrets
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from joblib import load
import re

# Load the dataset into a pandas dataframe
df = pd.read_excel(r'dataset.xlsx')

# Get all unique symptoms
symptoms = set()
for s in df['Symptoms']:
    for symptom in s.split(','):
        symptoms.add(symptom.strip())

def process_user_symptoms(symptoms):
    # Remove unwanted characters and split symptoms
    symptoms = re.sub(r'[^\w\s]', '', symptoms)  # Remove non-alphanumeric characters
    symptom_list = symptoms.split(',')
    return symptom_list

def predict_disease_from_symptom(symptom_list):
    user_symptoms = symptom_list
    # Vectorize symptoms using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['Symptoms'])
    user_X = vectorizer.transform([', '.join(user_symptoms)])

    # Compute cosine similarity between user symptoms and dataset symptoms
    similarity_scores = cosine_similarity(X, user_X)

    # Find the most similar disease(s)
    max_score = similarity_scores.max()
    max_indices = similarity_scores.argmax(axis=0)
    diseases = set()
    for i in max_indices:
        if similarity_scores[i] == max_score:
            diseases.add(df.iloc[i]['Disease'])

    # Output results
    if len(diseases) == 0:
        return "No matching diseases found"
    elif len(diseases) == 1:
        return list(diseases)[0]
    else:
        return "The most likely diseases are: " + ', '.join(list(diseases))

    user_symptoms = ', '.join(symptom_list)
    # Transform user symptoms using the recreated symptom encoder
    symptoms_encoded = symptom_encoder.transform([symptom_list])
    predicted_disease = model.predict(symptoms_encoded)
    return predicted_disease[0]

def get_symtoms(user_disease):
    # Vectorize diseases using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['Disease'])
    user_X = vectorizer.transform([user_disease])

    # Compute cosine similarity between user disease and dataset diseases
    similarity_scores = cosine_similarity(X, user_X)

    # Find the most similar disease(s)
    max_score = similarity_scores.max()
    if max_score < 0.7:
        return "No matching diseases found"
    else:
        max_indices = similarity_scores.argmax(axis=0)
        symptoms = set()
        for i in max_indices:
            if similarity_scores[i] == max_score:
                symptoms.update(set(df.iloc[i]['Symptoms'].split(',')))

        return "The symptoms of " + user_disease + " are: " + ', '.join(symptoms)

