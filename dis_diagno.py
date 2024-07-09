import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
import streamlit as st

# Define the model filename
model_filename = 'disease_model.pkl'

# Check if the model already exists
if not os.path.exists(model_filename):
    # Create and save the dataset
    data = {
        'fever': [1, 0, 1, 1, 0, 0, 1],
        'cough': [1, 1, 1, 0, 0, 1, 0],
        'fatigue': [1, 1, 0, 1, 0, 0, 1],
        'headache': [1, 0, 1, 1, 1, 0, 0],
        'disease': ['Flu', 'Cold', 'Flu', 'COVID-19', 'Cold', 'Healthy', 'COVID-19']
    }

    df = pd.DataFrame(data)
    df.to_csv('disease_data.csv', index=False)

    # Load the dataset
    df = pd.read_csv('disease_data.csv')

    # Features and target
    X = df.drop(columns=['disease'])
    y = df['disease']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, model_filename)

# Load the model
model = joblib.load(model_filename)

# Streamlit app
# Title and description
st.title('Disease Diagnosis App')
st.write('Enter your symptoms to get a diagnosis.')

# User input
fever = st.checkbox('Fever')
cough = st.checkbox('Cough')
fatigue = st.checkbox('Fatigue')
headache = st.checkbox('Headache')

# Convert input to dataframe
input_data = {
    'fever': int(fever),
    'cough': int(cough),
    'fatigue': int(fatigue),
    'headache': int(headache)
}
input_df = pd.DataFrame([input_data])

# Predict the disease
if st.button('Diagnose'):
    prediction = model.predict(input_df)
    st.write(f'You might have: {prediction[0]}')
