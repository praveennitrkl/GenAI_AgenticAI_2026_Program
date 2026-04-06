import streamlit as st
import numpy as np

from PIL import Image



st.title("My First Streamlit App")

st.header("Welcome to my Streamlit app!")
st.subheader("This is a subheader")

img = Image.open(r"C:\Users\Praveen Dheeraj\Downloads\DSC_5005.jpg")
st.image(img, caption="Dheeraj Namburu", width=200)

st.text("This is some sample text to demonstrate Streamlit's text display capabilities.")

st.markdown("You can also use **Markdown** to format your text. For example, you can make text *italic* or **bold**.")

st.write("You can write anything here, and Streamlit will render it appropriately. For example, you can include a list:")
st.write("- Item 1")
st.write("- Item 2")
st.write("- Item 3")
st.success("This is a success message!")
st.warning("This is a warning message!")
st.error("This is an error message!")
st.info("This is an informational message!")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

#st.write(np.arange(2,50,5))
l = [1,2,3,4,5]

#st.write(l)

rd = st.radio("Choose an option:", ("Option 1", "Option 2", "Option 3"))
if rd == "Option 1":
    st.success("You selected Option 1")
    
elif rd == "Option 2":
    st.success("You selected Option 2")

else:    st.success("You selected Option 3")

ckBox1 = st.checkbox("Check me out!")
ckBox2 = st.checkbox("Check me out too!")

if ckBox1:
    st.write("Checkbox 1 is checked!")
if ckBox2:
    st.write("Checkbox 2 is checked!")

bttn = st.button("Click me!")
if bttn:
    st.write("Button was clicked!")

clr = st.selectbox("Select a color:", ("Red", "Green", "Blue"), index=None)
st.write("You selected:", clr)

slct = st.multiselect("Select multiple options:", ["Option A", "Option B", "Option C"])
st.write("You selected:", len(slct), "Hobbies")

myname = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", myname, "! Welcome to Streamlit!")

slider = st.slider("Select Your Age:", 0, 100, 50)
st.write(f"Your age is: {slider}")
