import streamlit as st
import pandas as pd
import joblib

# ── Load model ──────────────────────────────────────────────
model = joblib.load("model.joblib")

# ── Page config ─────────────────────────────────────────────
st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢")
st.title("🚢 Titanic Survival Predictor")
st.markdown("Masukkan data penumpang untuk memprediksi kemungkinan selamat.")

# ── Input form ──────────────────────────────────────────────
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        pclass = st.selectbox("Ticket Class (Pclass)", options=[1, 2, 3],
                              format_func=lambda x: f"{x}st Class" if x == 1 else f"{x}nd Class" if x == 2 else "3rd Class")
        sex = st.selectbox("Sex", options=["male", "female"])
        embarked = st.selectbox("Port of Embarkation", options=["S", "C", "Q"],
                                format_func=lambda x: {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}[x])

    with col2:
        sibsp = st.number_input("Siblings / Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
        parch = st.number_input("Parents / Children Aboard (Parch)", min_value=0, max_value=10, value=0)
        fare = st.number_input("Passenger Fare (£)", min_value=0.0, max_value=600.0, value=32.0, step=0.5)

    submitted = st.form_submit_button("Predict", use_container_width=True)

# ── Prediction ──────────────────────────────────────────────
if submitted:
    input_data = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked
    }])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    st.divider()

    if prediction == 1:
        st.success("✅ **Survived** — Penumpang ini diprediksi **selamat**.")
    else:
        st.error("❌ **Not Survived** — Penumpang ini diprediksi **tidak selamat**.")

    col_a, col_b = st.columns(2)
    col_a.metric("Probabilitas Selamat", f"{proba[1]*100:.1f}%")
    col_b.metric("Probabilitas Tidak Selamat", f"{proba[0]*100:.1f}%")

    st.progress(float(proba[1]), text="Survival Probability")