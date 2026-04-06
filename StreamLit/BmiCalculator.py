import streamlit as st

# --- App Title and Description ---
st.title("BMI Calculator")
st.text("This app calculates your Body Mass Index (BMI) based on your weight and height.")

# --- Select Weight  Units---
weight_unit = st.radio("Choose Weight Unit:", ("Lbs (pounds)", "Kgs"), horizontal=True)

# ---- Input Weight ---
if weight_unit == "Lbs (pounds)":
    weight = st.number_input("Weight (Lbs (Pounds)):", min_value=0.0, format="%.2f") * 0.453592
else:
    weight = st.number_input("Weight (Kgs):", min_value=0.0, format="%.2f")


# ------ Select Height Units -----
height_unit = st.radio("Choose Height Unit:", ("Meters", "Centimeters", "Feet"),horizontal=True)

#------- Input Height -------
if height_unit == "Centimeters":
    height = st.number_input("Height (cm):", min_value=0.0, format="%.2f") / 100
elif height_unit == "Feet":
    height = st.number_input("Height (ft):", min_value=0.0, format="%.2f") * 0.3048
else:
    height = st.number_input("Height (m):", min_value=0.0, format="%.2f")

submitButton = st.button("Calculate")

if submitButton:
    try:
        if height<= 0:
            st.error("Height must be greater than zero.")
        else:
            bmi = weight / (height ** 2)
            st.success(f"Your BMI is {bmi:.2f}")
            
            if bmi < 16:
                st.error("You are Extremely Underweight")
            elif 16 <= bmi < 18.5:
                st.warning("You are Underweight")
            elif 18.5 <= bmi < 25:
                st.success("You are Healthy")
            elif 25 <= bmi < 30:
                st.warning("You are Overweight")
            else:
                st.error("You are Extremely Overweight")
    except:
        st.error("Please enter valid numeric values.")