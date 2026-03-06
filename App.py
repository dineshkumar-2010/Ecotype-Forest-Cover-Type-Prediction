import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(
    page_title="EcoType",
    page_icon="🌲",
    layout="wide"
)

# Centered Heading
st.markdown(
    "<h1 style='text-align: center;'>🌲 EcoType</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size:18px;'>Forest Cover Type Prediction</p>",
    unsafe_allow_html=True
)

st.markdown("")

# -----------------------------
# Load Model & Encoder
# -----------------------------
try:
    model = joblib.load("best_random_forest_model.pkl")
    label_encoder = joblib.load("label_encoder.pkl")
except:
    st.error("Model or encoder file not found.")
    st.stop()

feature_names = model.feature_names_in_

# -----------------------------
# Input Section (2 Columns)
# -----------------------------
st.subheader("Enter Environmental Features")

col1, col2 = st.columns(2)

data = {}

for i, feature in enumerate(feature_names):
    if i % 2 == 0:
        with col1:
            data[feature] = st.number_input(
                feature,
                min_value=0,
                value=0,
                step=1,
                format="%d"
            )
    else:
        with col2:
            data[feature] = st.number_input(
                feature,
                min_value=0,
                value=0,
                step=1,
                format="%d"
            )

input_df = pd.DataFrame([data])

st.markdown("")

# -----------------------------
# Prediction Button
# -----------------------------
center_col1, center_col2, center_col3 = st.columns([1,2,1])

with center_col2:
    if st.button("Predict Forest Type", use_container_width=True):

        try:
            prediction = model.predict(input_df)
            forest_type = label_encoder.inverse_transform(prediction)[0]

            st.success(f"🌳 Forest Cover Type: {forest_type}")

        except Exception as e:
            st.error("Prediction failed.")

