import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
def create_fraud_detector(title, csv_or_txt, what_it_looks_like_col, fraud_type_col):
    st.title(title)

    # User input
    Identify_Fraud_or_not = st.text_input(
        "Enter a mail"
    )

    # Dataset
    df = pd.read_csv(csv_or_txt)

    # Features and labels
    x = df[what_it_looks_like_col]
    y = df[fraud_type_col]

    # Convert text into numbers
    vectorizer = CountVectorizer()

    x_vectorized = vectorizer.fit_transform(x)

    # Train model
    model = MultinomialNB()

    model.fit(x_vectorized, y)

    # Prediction
    if Identify_Fraud_or_not:

        user_data = vectorizer.transform([Identify_Fraud_or_not])

        result = model.predict(user_data)

        if result[0] == "Safe":
            st.success("✅ This message looks safe.")
        else:
            st.error(f"⚠️ Fraud Detected: {result[0]}")
