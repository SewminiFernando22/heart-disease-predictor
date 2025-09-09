import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

# ===============================
# Load model and scaler
# ===============================
model = joblib.load('heart_model.pkl')
scaler = joblib.load('scaler.pkl')

# ===============================
# Custom CSS for styling
# ===============================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Background */
    .stApp {
        background: linear-gradient(135deg, #141e30, #243b55);
        color: white;
    }

    /* Card style for form */
    .stForm {
        background: rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    /* Sidebar style */
    .stSidebar {
        background: rgba(255, 255, 255, 0.08);
        padding: 15px;
        border-radius: 15px;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #ff4b4b, #ff6f61);
        color: white;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #e63946, #f77f00);
        transform: scale(1.05);
    }

    /* Progress bars */
    .stProgress > div > div > div > div {
        background-color: #ff4b4b;
    }

    /* Section headers */
    .section-header {
        color: #ff6f61;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 12px;
        text-shadow: 1px 1px 2px black;
    }

    /* Tips Box */
    .tips-box {
        background-color: #1e2a38;
        color: #f5f5f5;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
    }

    /* Custom Title */
    .app-title {
        font-family: 'Poppins', sans-serif;
        font-size: 48px;
        font-weight: 700;
        color: #ff4b4b;
        text-align: center;
        position: relative;
        margin-bottom: 5px;
    }
    .app-title::after {
        content: '';
        display: block;
        width: 200px;
        height: 5px;
        background: linear-gradient(90deg, #ff4b4b, #ff6f61);
        margin: 8px auto 0 auto;
        border-radius: 3px;
        animation: glow 2s infinite alternate;
    }
    @keyframes glow {
        from { box-shadow: 0 0 5px #ff6f61; }
        to { box-shadow: 0 0 15px #ff4b4b; }
    }
    .app-subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 20px;
        font-weight: 400;
        text-align: center;
        color: #f1f1f1;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# Title + Subtitle
# ===============================
st.markdown("""
    <div class="app-title">❤️ Heart Guardian </div>
    <div class="app-subtitle">Your Personal Heart Health Checker</div>
""", unsafe_allow_html=True)

st.image("https://source.unsplash.com/random/800x200/?heart,health", use_container_width=True)

# ===============================
# Sidebar - Quick Tips
# ===============================
with st.sidebar:
    st.header(" Quick Heart Tips")
    st.success(" Stay active: 30 mins/day")
    st.info(" Eat veggies & fruits")
    st.warning(" Monitor BP & cholesterol")
    st.image("https://source.unsplash.com/random/200x200/?fitness,heart", caption="Stay Healthy", use_container_width=True)

# ===============================
# Main Form
# ===============================
with st.form("patient_form"):
    # Section 1: Personal Information
    st.markdown('<div class="section-header"> Personal Info</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Your Age", min_value=20, max_value=80, value=50, help="Age in years")
        sex = st.selectbox("Sex", options=[("Female", 0), ("Male", 1)], format_func=lambda x: x[0])
    with col2:
        cp = st.selectbox("Chest Pain Type", options=[
            ("Typical Angina", 1), 
            ("Atypical Angina", 2), 
            ("Non-Anginal Pain", 3), 
            ("Asymptomatic", 4)], format_func=lambda x: x[0])

    # Section 2: Vital Signs
    st.markdown('<div class="section-header"> Vital Signs</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
        chol = st.slider("Cholesterol Level (mg/dl)", 100, 600, 200)
    with col4:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", [("No", 0), ("Yes", 1)], format_func=lambda x: x[0])
        thalach = st.slider("Max Heart Rate Achieved", 70, 220, 150)

    # Section 3: Test Results
    st.markdown('<div class="section-header"> Test Results</div>', unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        restecg = st.selectbox("Resting ECG Results", [("Normal", 0), ("ST-T Abnormality", 1), ("Hypertrophy", 2)], format_func=lambda x: x[0])
        exang = st.selectbox("Exercise-Induced Angina?", [("No", 0), ("Yes", 1)], format_func=lambda x: x[0])
        oldpeak = st.slider("ST Depression (oldpeak)", 0.0, 6.0, 1.0, step=0.1)
    with col6:
        slope = st.selectbox("ST Slope", [("Upsloping", 1), ("Flat", 2), ("Downsloping", 3)], format_func=lambda x: x[0])
        ca = st.selectbox("Major Vessels Colored (0-3)", [0, 1, 2, 3])
        thal = st.selectbox("Thalassemia Type", [("Normal", 3), ("Fixed Defect", 6), ("Reversible Defect", 7)], format_func=lambda x: x[0])

    # Submit button
    submitted = st.form_submit_button(" Predict My Heart Health!")

# ===============================
# Prediction Logic
# ===============================
if submitted:
    # Prepare input data
    input_data = np.array([[age, sex[1], cp[1], trestbps, chol, fbs[1], restecg[1], thalach, exang[1], oldpeak, slope[1], ca, thal[1]]])
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1] * 100  # Probability of disease

    # ===============================
    # Results
    # ===============================
    st.header(" Your Heart Health Results")

    if prediction == 0:
        st.success(" Great News! You're predicted to be HEALTHY.")
        st.balloons()
        st.progress(1.0 - (prob / 100))
        st.write(f"Risk Level: **Low** ({prob:.1f}% chance of heart disease)")
    else:
        st.warning(" Attention: You might have a HEART DISEASE RISK.")
        st.progress(prob / 100)
        st.write(f"Risk Level: **High** ({prob:.1f}% chance of heart disease)")

    # Gauge Chart (Plotly)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob,
        title={'text': "Heart Disease Risk (%)"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "red" if prob > 50 else "green"},
               'steps': [
                   {'range': [0, 50], 'color': "lightgreen"},
                   {'range': [50, 100], 'color': "lightcoral"}]}))
    st.plotly_chart(fig, use_container_width=True)

    # Tips
    st.markdown('<div class="tips-box">', unsafe_allow_html=True)
    st.subheader(" Personalized Health Tips")
    if prediction == 1:
        st.write("- **Monitor Closely**: Schedule a doctor's visit soon.")
        st.write("- **Lifestyle Changes**: Reduce stress, quit smoking, and exercise more.")
    else:
        st.write("- **Maintain It**: Keep up your healthy habits!")
        st.write("- **Preventive Care**: Regular check-ups are key.")
    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# Footer
# ===============================
st.markdown("---")
st.write("@SewminiFernando | Data from UCI Heart Disease Dataset | For educational purposes only.")
st.markdown("“Take care of your heart, and it will take care of you.” 💖")
