
from pathlib import Path
import pickle

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Electricity Bill Predictor | Sufiyan",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE = Path(__file__).resolve().parent
MODEL_PATH = BASE / "electricity_bill_model.pkl"
DATA_PATH = BASE / "electricity_bill_dataset.csv"


# ==================================================
# COMPACT CSS - LESS EMPTY SPACE
# ==================================================
st.markdown("""
<style>
    #MainMenu, footer, [data-testid="stSidebar"] {
        display: none !important;
    }

    header[data-testid="stHeader"] {
        height: 2rem;
        background: transparent;
    }

    .stApp {
        background: #f2f6fc;
        color: #17243a;
    }

    .block-container {
        max-width: 1500px;
        padding: 0.8rem 1.3rem 1rem 1.3rem !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 0.65rem;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 1rem;
    }

    h1, h2, h3, h4, p, label {
        color: #17243a;
    }

    h1 {
        font-size: 2rem !important;
    }

    h2, h3 {
        margin-top: 0.2rem !important;
        margin-bottom: 0.35rem !important;
    }

    .hero {
        background: linear-gradient(115deg, #123f80, #0786a8);
        border-radius: 16px;
        padding: 18px 24px;
        margin-bottom: 10px;
        box-shadow: 0 5px 18px rgba(15, 60, 129, 0.12);
    }

    .hero h1 {
        color: #ffffff !important;
        margin: 0 !important;
        line-height: 1.25;
    }

    .hero p {
        color: #ffffff !important;
        margin: 5px 0 0 0 !important;
        font-size: 0.95rem;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #123f80;
        margin: 0 0 4px 0;
    }

    .compact-card {
        background: #ffffff;
        border: 1px solid #dce5f0;
        border-radius: 14px;
        padding: 15px 17px;
        margin-bottom: 8px;
        box-shadow: 0 3px 12px rgba(25, 50, 80, 0.045);
    }

    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #dce5f0;
        border-radius: 11px;
        padding: 10px 12px;
    }

    div[data-testid="stMetricLabel"] {
        color: #42526b !important;
    }

    div[data-testid="stMetricValue"] {
        color: #123f80 !important;
        font-size: 1.45rem !important;
    }

    div[data-testid="stForm"] {
        border: none;
        padding: 0;
    }

    div[data-testid="stFormSubmitButton"] > button,
    div.stDownloadButton > button {
        background: #087eaa;
        color: white;
        border: none;
        border-radius: 9px;
        min-height: 40px;
        font-weight: 600;
        width: 100%;
    }

    div[data-testid="stFormSubmitButton"] > button:hover,
    div.stDownloadButton > button:hover {
        background: #075b85;
        color: white;
    }

    [data-testid="stAlert"] {
        border-radius: 10px;
    }

    .footer {
        text-align: center;
        color: #52627a;
        border-top: 1px solid #dce5f0;
        padding: 12px 0 0 0;
        margin-top: 12px;
        font-size: 0.88rem;
    }

    @media (max-width: 900px) {
        .block-container {
            padding: 0.6rem !important;
        }

        .hero {
            padding: 16px;
        }

        .hero h1 {
            font-size: 1.6rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)


# ==================================================
# GRAPH STYLE
# ==================================================
def fix_graph_text(fig):
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="#17243a"
        ),
        title_font=dict(size=16, color="#17243a"),
        margin=dict(l=55, r=18, t=55, b=55),
        legend=dict(
            font=dict(color="#17243a"),
            bgcolor="#ffffff"
        )
    )

    fig.update_xaxes(
        title_font=dict(size=12, color="#17243a"),
        tickfont=dict(size=11, color="#253750"),
        showline=True,
        linecolor="#94a3b8",
        gridcolor="#e2e8f0",
        automargin=True
    )

    fig.update_yaxes(
        title_font=dict(size=12, color="#17243a"),
        tickfont=dict(size=11, color="#253750"),
        showline=True,
        linecolor="#94a3b8",
        gridcolor="#e2e8f0",
        automargin=True
    )

    return fig


# ==================================================
# LOAD MODEL
# ==================================================
@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)


# ==================================================
# LOAD DATASET
# ==================================================
@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    required = [
        "MonthlyHours",
        "TariffRate",
        "ElectricityBill"
    ]

    missing = [col for col in required if col not in df.columns]

    if missing:
        raise ValueError(
            "Required dataset columns missing: "
            + ", ".join(missing)
            + "\nAvailable columns: "
            + ", ".join(df.columns.astype(str))
        )

    for col in required:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=required).copy()

    # Generate BaseCost even when it is absent from the CSV.
    df["BaseCost"] = df["MonthlyHours"] * df["TariffRate"]

    return df


# ==================================================
# HEADER
# ==================================================
st.markdown("""
<div class="hero">
    <h1>⚡ Electricity Bill Predictor</h1>
    <p>Estimate your monthly electricity bill with Machine Learning.</p>
    <p>Designed and developed by Sufiyan</p>
</div>
""", unsafe_allow_html=True)


# ==================================================
# LOAD FILES AND SHOW CLEAR ERRORS
# ==================================================
try:
    model = load_model()
    dataset = load_data()
except Exception as error:
    st.error("App could not load. Check the error below.")
    st.code(str(error))
    st.stop()


# ==================================================
# MAIN LAYOUT - COMPACT SIDE BY SIDE
# ==================================================
left_col, right_col = st.columns(
    [0.85, 1.65],
    gap="medium"
)


# ==================================================
# LEFT: BILL INPUT
# ==================================================
with left_col:
    st.markdown(
        '<div class="section-title">🧮 Calculate Your Bill</div>',
        unsafe_allow_html=True
    )

    st.caption("Enter your monthly usage and tariff rate.")

    with st.container(border=True):
        with st.form("bill_prediction_form"):
            hours = st.number_input(
                "Monthly Usage (hours)",
                min_value=1,
                max_value=744,
                value=200,
                step=10
            )

            rate = st.number_input(
                "Tariff Rate (₹ per unit)",
                min_value=0.01,
                max_value=1000.0,
                value=15.0,
                step=0.5,
                format="%.2f"
            )

            submitted = st.form_submit_button(
                "⚡ Predict Electricity Bill",
                use_container_width=True
            )

        st.caption("BaseCost = MonthlyHours × TariffRate")

    if submitted:
        try:
            input_df = pd.DataFrame({
                "MonthlyHours": [float(hours)],
                "TariffRate": [float(rate)],
                "BaseCost": [float(hours) * float(rate)]
            })

            # Match the exact feature order saved in the model.
            if hasattr(model, "feature_names_in_"):
                model_features = list(model.feature_names_in_)
                missing_features = [
                    feature for feature in model_features
                    if feature not in input_df.columns
                ]

                if missing_features:
                    raise ValueError(
                        "Model requires different features. Expected: "
                        + ", ".join(model_features)
                    )

                input_df = input_df[model_features]

            prediction = float(model.predict(input_df)[0])

            st.session_state["prediction"] = max(0.0, prediction)
            st.session_state["input_hours"] = float(hours)
            st.session_state["input_rate"] = float(rate)

        except Exception as error:
            st.error("Prediction failed.")
            st.code(str(error))


# ==================================================
# RIGHT: PREDICTION DASHBOARD
# ==================================================
with right_col:
    st.markdown(
        '<div class="section-title">📊 Prediction Dashboard</div>',
        unsafe_allow_html=True
    )

    if "prediction" in st.session_state:
        predicted = st.session_state["prediction"]
        used_hours = st.session_state["input_hours"]
        used_rate = st.session_state["input_rate"]
        calculated = used_hours * used_rate

        m1, m2, m3 = st.columns(3)

        m1.metric("Predicted Bill", f"₹{predicted:,.2f}")
        m2.metric("Monthly Hours", f"{used_hours:,.0f}")
        m3.metric("Tariff Rate", f"₹{used_rate:,.2f}")

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Model Prediction"],
            y=[predicted],
            name="Predicted Bill",
            marker_color="#087eaa",
            text=[f"₹{predicted:,.2f}"],
            textposition="outside",
            textfont=dict(color="#17243a", size=12)
        ))

        fig.add_trace(go.Bar(
            x=["Hours × Tariff"],
            y=[calculated],
            name="Hours × Tariff",
            marker_color="#22a06b",
            text=[f"₹{calculated:,.2f}"],
            textposition="outside",
            textfont=dict(color="#17243a", size=12)
        ))

        fig.update_layout(
            title="Predicted Bill vs Basic Calculation",
            xaxis_title="Calculation Method",
            yaxis_title="Amount (₹)",
            showlegend=False,
            height=310,
            bargap=0.45
        )

        st.plotly_chart(
            fix_graph_text(fig),
            use_container_width=True,
            config={"displayModeBar": False}
        )

        report = pd.DataFrame({
            "MonthlyHours": [used_hours],
            "TariffRate": [used_rate],
            "BaseCost": [calculated],
            "PredictedElectricityBill": [predicted]
        })

        st.download_button(
            "⬇️ Download Prediction Report",
            data=report.to_csv(index=False).encode("utf-8"),
            file_name="electricity_bill_prediction.csv",
            mime="text/csv",
            use_container_width=True
        )

    else:
        st.info(
            "Enter your details on the left and click "
            "'Predict Electricity Bill'."
        )

        demo = go.Figure()

        demo.add_trace(go.Bar(
            x=["100 hours", "200 hours", "300 hours"],
            y=[1500, 3000, 4500],
            marker_color=["#087eaa", "#22a06b", "#e7a23b"],
            text=["₹1,500", "₹3,000", "₹4,500"],
            textposition="outside",
            textfont=dict(color="#17243a", size=12)
        ))

        demo.update_layout(
            title="Example Electricity Bill",
            xaxis_title="Example Monthly Usage",
            yaxis_title="Example Amount (₹)",
            showlegend=False,
            height=310
        )

        st.plotly_chart(
            fix_graph_text(demo),
            use_container_width=True,
            config={"displayModeBar": False}
        )


# ==================================================
# MODEL PERFORMANCE
# ==================================================
st.divider()

st.markdown(
    '<div class="section-title">📈 Model Performance</div>',
    unsafe_allow_html=True
)

st.caption("Evaluation on a held-out dataset split.")

try:
    X = dataset[["MonthlyHours", "TariffRate", "BaseCost"]]
    y = dataset["ElectricityBill"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=0
    )

    if hasattr(model, "feature_names_in_"):
        features = list(model.feature_names_in_)
        missing = [col for col in features if col not in X_test.columns]

        if missing:
            raise ValueError(
                "Model evaluation requires different columns: "
                + ", ".join(features)
            )

        X_test = X_test[features]

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    s1, s2, s3 = st.columns(3)

    s1.metric("R² Score", f"{r2:.4f}")
    s2.metric("Mean Absolute Error", f"₹{mae:,.2f}")
    s3.metric("RMSE", f"₹{rmse:,.2f}")

    actual_values = y_test.iloc[:25].to_numpy()
    predicted_values = np.asarray(y_pred)[:25]
    records = list(range(1, len(actual_values) + 1))

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=records,
        y=actual_values,
        mode="lines+markers",
        name="Actual Bill",
        line=dict(color="#087eaa", width=2)
    ))

    fig2.add_trace(go.Scatter(
        x=records,
        y=predicted_values,
        mode="lines+markers",
        name="Predicted Bill",
        line=dict(color="#e7a23b", width=2)
    ))

    fig2.update_layout(
        title="Actual vs Predicted Bills (First 25 Test Rows)",
        xaxis_title="Test Record",
        yaxis_title="Electricity Bill (₹)",
        height=340
    )

    st.plotly_chart(
        fix_graph_text(fig2),
        use_container_width=True,
        config={"displayModeBar": False}
    )

except Exception as error:
    st.warning("Model performance could not be calculated.")
    st.code(str(error))


# ==================================================
# DATASET PREVIEW
# ==================================================
with st.expander("📁 Dataset Overview"):
    st.write(f"Valid records: {len(dataset):,}")
    st.dataframe(dataset.head(10), use_container_width=True)


# ==================================================
# FOOTER
# ==================================================
st.markdown("""
<div class="footer">
    ⚡ Electricity Bill Predictor · Created by <b>Sufiyan</b><br>
    Python · Machine Learning · Streamlit · Plotly
</div>
""", unsafe_allow_html=True)
