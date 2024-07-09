import streamlit as st
import pandas as pd
import datetime
from collections import defaultdict

# Initialize session state
if 'meals' not in st.session_state:
    st.session_state.meals = []

# Function to add a meal
def add_meal():
    meal = {
        'date': st.session_state.date,
        'meal_type': st.session_state.meal_type,
        'food': st.session_state.food,
        'calories': st.session_state.calories,
        'protein': st.session_state.protein,
        'carbs': st.session_state.carbs,
        'fats': st.session_state.fats
    }
    st.session_state.meals.append(meal)
    st.session_state.food = ''
    st.session_state.calories = 0
    st.session_state.protein = 0
    st.session_state.carbs = 0
    st.session_state.fats = 0

# Streamlit app
st.title("Nutrition Tracker")

st.header("Log a Meal")

# Input fields for meal logging
st.session_state.date = st.date_input("Date", datetime.date.today())
st.session_state.meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack"])
st.session_state.food = st.text_input("Food", key="food")
st.session_state.calories = st.number_input("Calories", min_value=0, step=1, key="calories")
st.session_state.protein = st.number_input("Protein (g)", min_value=0, step=1, key="protein")
st.session_state.carbs = st.number_input("Carbohydrates (g)", min_value=0, step=1, key="carbs")
st.session_state.fats = st.number_input("Fats (g)", min_value=0, step=1, key="fats")

# Add meal button
if st.button("Add Meal"):
    add_meal()
    st.success("Meal added successfully!")

# Display logged meals
st.header("Logged Meals")

if st.session_state.meals:
    meals_df = pd.DataFrame(st.session_state.meals)
    st.table(meals_df)

    # Summary statistics
    st.header("Summary Statistics")
    total_calories = meals_df['calories'].sum()
    total_protein = meals_df['protein'].sum()
    total_carbs = meals_df['carbs'].sum()
    total_fats = meals_df['fats'].sum()

    st.write(f"Total Calories: {total_calories} kcal")
    st.write(f"Total Protein: {total_protein} g")
    st.write(f"Total Carbohydrates: {total_carbs} g")
    st.write(f"Total Fats: {total_fats} g")
else:
    st.write("No meals logged yet.")
