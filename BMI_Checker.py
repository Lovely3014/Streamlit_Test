import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    return weight / (height ** 2)

def get_health_tips(bmi, diet_preference):
    """Return health tips based on BMI and diet preference."""
    if bmi < 18.5:
        tips = "You are underweight. Consider increasing your calorie intake with nutritious foods."
    elif 18.5 <= bmi < 24.9:
        tips = "You have a normal weight. Maintain your healthy lifestyle!"
    elif 25 <= bmi < 29.9:
        tips = "You are overweight. Consider adopting a healthier diet and increasing physical activity."
    else:
        tips = "You are obese. Seek advice from a healthcare provider for a suitable weight loss plan."

    if diet_preference == "Vegetarian":
        tips += "\n\n**Vegetarian Tips:**\n- Include a variety of protein sources like beans, lentils, tofu, and nuts.\n- Ensure you get enough iron from foods like spinach, lentils, and fortified cereals.\n- Consider vitamin B12 supplements if you're not consuming dairy or eggs."
    else:
        tips += "\n\n**Non-Vegetarian Tips:**\n- Choose lean meats like chicken and fish over red and processed meats.\n- Include plenty of vegetables and fruits in your meals.\n- Be mindful of portion sizes and avoid high-fat cooking methods like frying."

    return tips

def main():
    st.title("BMI Checker and Health Tips")

    # Input fields for weight and height
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height (m)", min_value=0.1, step=0.01)

    # Input for diet preference
    diet_preference = st.radio("Select your diet preference", ("Vegetarian", "Non-Vegetarian"))

    # Calculate BMI and provide health tips
    if st.button("Calculate BMI"):
        if height > 0 and weight > 0:
            bmi = calculate_bmi(weight, height)
            st.write(f"Your BMI is: {bmi:.2f}")

            health_tips = get_health_tips(bmi, diet_preference)
            st.write(health_tips)
        else:
            st.warning("Please enter valid weight and height values.")

if __name__ == "__main__":
    main()
