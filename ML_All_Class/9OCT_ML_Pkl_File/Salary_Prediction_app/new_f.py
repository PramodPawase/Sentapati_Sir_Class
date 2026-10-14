
import pickle
from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st

# ============== PAGE CONFIG ==============
st.set_page_config(
    page_title="SalaryWise AI | Salary Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============== MODEL PATH ==============
MODEL_PATH = Path(__file__).resolve().parent / "Linear_r_m.pkl"


@st.cache_resource
def load_model():
    with MODEL_PATH.open("rb") as file:
        return pickle.load(file)


# ============== CUSTOM CSS ==============
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --cyan: #45d9ff;
    --purple: #a94aff;
    --text: #f5f7ff;
    --muted: #adbad9;
}

.stApp {
    background:
        radial-gradient(ellipse at top left, #172b65, transparent 48%),
        radial-gradient(ellipse at top right, #32145b, transparent 42%),
        #070d1d;
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1120px;
    padding: 0.8rem 1.4rem 1rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3, p, label {
    color: var(--text);
}

.brand {
    font-size: 24px;
    font-weight: 800;
    letter-spacing: -0.8px;
}

.cyan { color: var(--cyan); }
.purple { color: #c18aff; }

.hero {
    font-size: clamp(30px, 3.5vw, 43px);
    line-height: 1.12;
    font-weight: 800;
    letter-spacing: -1.4px;
    margin: 12px 0 8px;
}

.muted {
    color: var(--muted);
    font-size: 13px;
    line-height: 1.65;
}

.pill {
    display: inline-block;
    border: 1px solid #3865b5;
    background: rgba(16, 38, 76, 0.8);
    color: #77e7ff;
    border-radius: 30px;
    padding: 6px 11px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
}

.card {
    background: linear-gradient(
        135deg,
        rgba(31, 61, 111, 0.68),
        rgba(20, 20, 54, 0.82)
    );
    border: 1px solid rgba(93, 157, 255, 0.48);
    border-radius: 16px;
    padding: 17px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    overflow-wrap: anywhere;
}

.result {
    font-size: clamp(28px, 3vw, 39px);
    line-height: 1.2;
    font-weight: 800;
    overflow-wrap: anywhere;
    background: linear-gradient(90deg, #ffffff, #57dfff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 8px 0;
}

.label {
    color: #77e7ff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* Proper Streamlit input card */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(
        135deg,
        rgba(31, 61, 111, 0.65),
        rgba(20, 20, 54, 0.78)
    );
    border: 1px solid rgba(93, 157, 255, 0.5);
    border-radius: 15px;
    padding: 14px 15px;
}

/* Input field */
div[data-testid="stNumberInput"] {
    margin-top: 5px;
}

div[data-testid="stNumberInput"] input {
    background: #111f40;
    color: white;
    border: 1px solid #4766a3;
    border-radius: 9px;
    min-height: 42px;
}

div[data-testid="stNumberInput"] button {
    background: #192d54;
    color: white;
}

/* Prediction button */
div.stButton > button {
    width: 100%;
    min-height: 44px;
    border: 0;
    border-radius: 10px;
    background: linear-gradient(
        100deg, #11bfe9, #5357ff, #a94aff
    );
    color: white;
    font-weight: 700;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    color: white;
    border: 1px solid #8feaff;
    box-shadow: 0 4px 18px #575cff50;
    transform: translateY(-1px);
}

/* Consistent layout spacing */
div[data-testid="stHorizontalBlock"] {
    align-items: flex-start;
    gap: 1.2rem;
}

div[data-testid="stVerticalBlock"] {
    gap: 0.65rem;
}

hr {
    border-color: #26395e;
    margin: 12px 0;
}

#MainMenu, footer {
    visibility: hidden;
}

@media (max-width: 700px) {
    .block-container {
        padding: 0.6rem 0.8rem 1rem;
    }

    .brand {
        font-size: 20px;
    }

    .hero {
        font-size: 32px;
    }

    .card {
        padding: 14px;
    }
}
</style>
""", unsafe_allow_html=True)


# ============== HEADER ==============
header1, header2 = st.columns([1.5, 1])

with header1:
    st.markdown(
        '<div class="brand">📊 SALARY'
        '<span class="cyan">WISE</span> '
        '<span class="purple">AI</span></div>',
        unsafe_allow_html=True
    )

with header2:
    st.markdown(
        '<div style="text-align:right;padding-top:7px;">'
        '<span class="pill">LINEAR REGRESSION</span></div>',
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)


# ============== MAIN DASHBOARD ==============
left, right = st.columns([1, 1], gap="medium")


# ============== LEFT: INPUT ==============
with left:
    st.markdown(
        '<span class="pill">✦ SMART SALARY PREDICTOR</span>'
        '<div class="hero">Know Your '
        '<span class="cyan">Worth.</span></div>'
        '<p class="muted">Estimate your annual salary using your '
        'years of professional experience and a trained ML model.</p>',
        unsafe_allow_html=True
    )

    # A real Streamlit container keeps widgets inside the card
    with st.container(border=True):
        st.markdown(
            '<div class="label">💼 YEARS OF EXPERIENCE</div>',
            unsafe_allow_html=True
        )

        st.caption("Enter your total professional experience in years.")

        experience = st.number_input(
            "Years of experience",
            min_value=0.0,
            max_value=50.0,
            value=1.0,
            step=0.5,
            label_visibility="collapsed",
            key="experience_input"
        )

        predict_clicked = st.button(
            "✦  PREDICT MY SALARY  →",
            use_container_width=True
        )

    st.markdown(
        '<p class="muted">🔒 Machine Learning · Built by SAYYED</p>',
        unsafe_allow_html=True
    )


# ============== RIGHT: RESULT & CHART ==============
with right:
    try:
        model = load_model()

        if (
            predict_clicked
            or "salary_prediction" not in st.session_state
        ):
            prediction = model.predict(
                np.array([[experience]], dtype=float)
            )

            st.session_state.salary_prediction = float(
                np.asarray(prediction).reshape(-1)[0]
            )
            st.session_state.salary_experience = experience

        salary = st.session_state.salary_prediction
        used_experience = st.session_state.salary_experience

        st.markdown(f"""
        <div class="card">
            <div class="label">✦ PREDICTED ANNUAL SALARY</div>
            <div class="result">${salary:,.2f}</div>
            <div style="color:#4be6b0;font-size:13px;font-weight:600;">
                ↗ Estimated by your ML model
            </div>
            <hr>
            <div class="muted">
                Experience: <b>{used_experience:.1f} years</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📈 Salary Growth")

        chart_years = np.arange(0, 11, dtype=float)

        chart_predictions = model.predict(
            chart_years.reshape(-1, 1)
        )

        chart_df = pd.DataFrame({
            "Years": chart_years,
            "Predicted salary": np.asarray(
                chart_predictions
            ).reshape(-1)
        }).set_index("Years")

        st.line_chart(
            chart_df,
            color="#45d9ff",
            height=210
        )

    except FileNotFoundError:
        st.error(
            "Model file not found. Place Linear_r_m.pkl "
            "in the same folder as new f.py."
        )

    except Exception as error:
        st.error(f"Prediction error: {error}")


# ============== FOOTER CARDS ==============
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### ✨ About Your Prediction")

info1, info2 = st.columns(2, gap="medium")

with info1:
    st.markdown("""
    <div class="card">
        <div class="label">📊 ABOUT THE MODEL</div>
        <p class="muted">
            Linear Regression estimates salary from years of experience
            using the data supplied during model training.
        </p>
    </div>
    """, unsafe_allow_html=True)

with info2:
    st.markdown("""
    <div class="card">
        <div class="label">🛡️ IMPORTANT NOTE</div>
        <p class="muted">
            This is an estimate, not a guaranteed salary. Actual pay
            depends on location, skills, company and industry.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center;color:#788bad;font-size:11px;margin-top:14px;">
    SALARYWISE AI · MACHINE LEARNING PROJECT · © SAYYED
</p>
""", unsafe_allow_html=True)
