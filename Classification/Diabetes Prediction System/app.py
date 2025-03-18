import streamlit as st
import pickle
import numpy as np

# Load model and encoders
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('ohe_smoke.pkl', 'rb') as file:
    ohe_smoke = pickle.load(file)

with open('ohe_drink.pkl', 'rb') as file:
    ohe_drink = pickle.load(file)

with open('StandardScaler.pkl', 'rb') as file:
    Ss = pickle.load(file)

# Set full width for the page
st.set_page_config(layout="wide")


st.markdown(
    """
    <h1 style="text-align: center; color: purple;">🩺 Smart Diabetes Prediction System 🔬</h1>
    """,
    unsafe_allow_html=True
)

# Increase the size of input fields using custom CSS
st.markdown(
    """
    <style>
    .stNumberInput input {
        font-size: 18px !important;
        height: 40px !important;
    }
    .stSelectbox div {
        font-size: 20px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Increase input box size */
    .stNumberInput input {
        font-size: 25px !important;
        height: 50px !important;
        padding: 30px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)




# Create three columns for better spacing
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown("<div style='text-align: center;'><h3>Age (Years) 🧑 </h3></div>", unsafe_allow_html=True)
    age = st.number_input(" ", min_value=0, max_value=120, step=1, key="age")

    st.markdown("<div style='text-align: center;'><h3>Gender ⚥ </h3></div>", unsafe_allow_html=True)
    gender = st.selectbox(" ", ["Male", "Female"], key="gender")

    st.markdown("<div style='text-align: center;'><h3>Body Mass Index (BMI) ⚖️ </h3></div>", unsafe_allow_html=True)
    bmi = st.number_input(" ", min_value=0.0, max_value=50.0, step=0.1, key="bmi")

    st.markdown("<div style='text-align: center;'><h3>Systolic Blood Pressure (SBP) mmHg 💓 </h3></div>", unsafe_allow_html=True)
    sbp = st.number_input(" ", min_value=50, max_value=200, step=1, key="sbp")

    st.markdown("<div style='text-align: center;'><h3>Diastolic Blood Pressure (DBP) mmHg 🩸 </h3></div>", unsafe_allow_html=True)
    dbp = st.number_input(" ", min_value=30, max_value=150, step=1, key="dbp")

with col2:
    st.markdown("<div style='text-align: center;'><h3>Fasting Plasma Glucose (FPG) mmol/L 🩺 </h3></div>", unsafe_allow_html=True)
    fpg = st.number_input(" ", min_value=0.0, max_value=50.0, step=0.1, key="fpg")

    st.markdown("<div style='text-align: center;'><h3>Total Cholesterol (mg/dL) 🫀 </h3></div>", unsafe_allow_html=True)
    chol = st.number_input(" ", min_value=0.0, max_value=50.0, step=0.1, key="chol")

    st.markdown("<div style='text-align: center;'><h3>Triglycerides (mg/dL) 🫁 </h3></div>", unsafe_allow_html=True)
    tri = st.number_input(" ", min_value=0.0, max_value=50.0, step=0.1, key="tri")

    st.markdown("<div style='text-align: center;'><h3>High-Density Lipoprotein (HDL) mg/dL 💙 </h3></div>", unsafe_allow_html=True)
    hdl = st.number_input(" ", min_value=0.0, max_value=50.0, step=0.1, key="hdl")

    st.markdown("<div style='text-align: center;'><h3>Low-Density Lipoprotein (LDL) mg/dL 💔 </h3></div>", unsafe_allow_html=True)
    ldl = st.number_input(" ", min_value=0.0, max_value=50.0, step=0.1, key="ldl")

with col3:
    st.markdown("<div style='text-align: center;'><h3>Blood Urea Nitrogen (BUN) mg/dL 🦾 </h3></div>", unsafe_allow_html=True)
    bun = st.number_input(" ", min_value=0.0, max_value=50.0, step=0.1, key="bun")

    st.markdown("<div style='text-align: center;'><h3>Fasting Finger-Prick Glucose(FFPG)mmol/L🧪</h3></div>", unsafe_allow_html=True)
    ffpg = st.number_input(" ", min_value=0.0, max_value=50.0, step=0.1, key="ffpg")

    st.markdown("<div style='text-align: center;'><h3>Smoking Status 🚬 </h3></div>", unsafe_allow_html=True)
    smoking = st.selectbox(" ", ["Never Smoked", "Once upon a time", "Occasional Smoker", "Daily Smoker"], key="smoking")

    st.markdown("<div style='text-align: center;'><h3>Drinking Status 🍺 </h3></div>", unsafe_allow_html=True)
    drinking = st.selectbox(" ", ["Never Drank", "Once upon a time", "Occasional Drinker", "Daily Drinker"], key="drinking")

    st.markdown("<div style='text-align: center;'><h3>Family History of Disease 🏥 </h3></div>", unsafe_allow_html=True)
    family_history = st.selectbox(" ", ["Yes", "No"], key="family_history")


st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #87CEFA !important; /* Light Blue */
        color: black !important;
        border-radius: 50px;
        padding: 8px 18px; /* Increased button size */
        font-weight: bold;
        font-size: 24px !important; /* Enforce larger font */
        transform: scale(1.5); /* Scale the button up */
        border: none;
        transition: background-color 0.3s ease-in-out, transform 0.1s ease-in-out;
    }

    div.stButton > button:first-child:active {
        background-color: #4682B4 !important; /* Darker Blue on Click */
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("🔎 Check Diabetes 🧬"):
    sample_input = [age, gender, bmi, sbp, dbp, fpg, chol, tri, hdl, ldl, bun, ffpg, smoking, drinking, family_history]
    sample_input[-1] = 1 if sample_input[-1] == "Yes" else 0 

    # Preprocessing Steps
    sample_input.pop(1)
    a = ohe_smoke.transform([[sample_input[11]]])[0]
    sample_input.pop(11)
    sample_input.extend(a)

    z = ohe_drink.transform([[sample_input[11]]])[0]
    z = list(z)
    sample_input.pop(11)
    sample_input.extend(z)

    columns = [1, 2, 3, 4]
    values = np.array([sample_input[i] for i in columns])
    val = Ss.transform([values])
    b = list(val[0])

    for i in columns:
        sample_input.pop(i)
        sample_input.insert(i, b[i-1])

    sample_input = np.array(sample_input, dtype=float).reshape(1, -1)
    out = model.predict(sample_input)[0]

    if out == 0:
        st.markdown(
            "<div style='background-color: #EAF8ED; color: black; padding: 25px; border-radius: 10px; text-align: center; width: 50%; margin: auto;'>"
            "<h2>✅ No Diabetes Detected</h2></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background-color: #FCE8E6; color: black; padding: 25px; border-radius: 10px; text-align: center; width: 50%; margin: auto;'>"
            "<h2>🚨 Diabetes Detected</h2></div>",
            unsafe_allow_html=True
        )
