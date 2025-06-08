import streamlit as st

st.set_page_config(page_title="Tiranga Predictor", layout="centered")
st.title("🔮 Tiranga Predictor")
st.markdown("Enter the **last Period Number**, and get the prediction instantly.")

period = st.text_input("Enter Period Number", "")

if period.isdigit():
    number = int(period[-1])
    if number == 0:
        color = "Red or Violet"
    elif number == 5:
        color = "Green or Violet"
    elif number % 2 == 0:
        color = "Red"
    else:
        color = "Green"

    size = "Big" if number > 4 else "Small"

    st.success(f"**Prediction:**")
    st.write(f"🔢 **Number:** {number}")
    st.write(f"🎨 **Color:** {color}")
    st.write(f"📏 **Size:** {size}")
elif period:
    st.error("Please enter a valid numeric Period Number")
