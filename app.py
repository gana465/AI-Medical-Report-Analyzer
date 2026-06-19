import streamlit as st

st.set_page_config(
    page_title="Medical Report Analyzer AI",
    page_icon="🩺",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(135deg,#07152d,#152548);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#64C8F7,#4D97F5);
}

/* Sidebar headings */
.black-heading{
    color:black !important;
    font-size:28px;
    font-weight:700;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"]{
    background:white !important;
    border-radius:12px;
}

/* Selected disease text */
.stSelectbox div[data-baseweb="select"] span{
    color:black !important;
    font-weight:600 !important;
}

/* Dropdown arrow */
.stSelectbox svg{
    fill:black !important;
}

/* Number Inputs */
.stNumberInput input{
    background:white !important;
    color:black !important;
}

/* Labels */
label[data-testid="stWidgetLabel"] p{
    color:white !important;
    font-size:16px !important;
    font-weight:600 !important;
}

/* Metric Cards */
.metric-card{
    background:rgba(255,255,255,0.08);
    border-radius:20px;
    padding:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
}

.metric-card h3{
    color:white;
}

.metric-card h2{
    color:#60A5FA;
}

/* Button */
.stButton button{
    width:100%;
    height:60px;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#27B8FF,#2563EB);
    color:white;
    font-size:20px;
    font-weight:bold;
}

/* Result Card */
.result-card{
    background:white;
    padding:25px;
    border-radius:20px;
}

.result-card *{
    color:black !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
[data-testid="stCaptionContainer"]{
    color:#94A3B8 !important;
    font-size:13px !important;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:

    st.markdown("""
    <div style='text-align:center'>
        <h1>🩺</h1>
        <h2 style='color:white;'>Medical AI</h2>
        <p style='color:white;'>Smart Healthcare Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        "<p class='black-heading'>🩺 Select Disease</p>",
        unsafe_allow_html=True
    )

    disease = st.selectbox(
        "",
        [
            "Chronic Kidney Disease",
        ],
        label_visibility="collapsed"
    )

    
# ================= HEADER =================
st.markdown("""
<h1 style='text-align:center;color:#60A5FA;'>
🩺 Medical Report Analyzer AI
</h1>
<h3 style='text-align:center;color:#D1D5DB;'>
AI Powered Health Risk Assessment System
</h3>
""", unsafe_allow_html=True)

st.write("")

# ================= INPUTS =================
# ================= PATIENT INFORMATION =================

st.markdown(
    "<h2 style='color:white;'>📋 Patient Information</h2>",
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    age = st.number_input("Age", 1, 120, 30)
    st.caption("Normal Range: 1 - 120 Years")

    bp = st.number_input("Blood Pressure", 50, 250, 120)
    st.caption("Normal Range: 90 - 140 mmHg")

    glucose = st.number_input("Glucose", 50, 500, 100)
    st.caption("Normal Range: 70 - 140 mg/dL")

with c2:
    creatinine = st.number_input("Creatinine", 0.1, 20.0, 1.0)
    st.caption("Normal Range: 0.6 - 1.3 mg/dL")

    urea = st.number_input("Blood Urea", 1, 300, 40)
    st.caption("Normal Range: 15 - 45 mg/dL")

    sodium = st.number_input("Sodium", 100, 170, 140)
    st.caption("Normal Range: 135 - 145 mEq/L")

with c3:
    potassium = st.number_input("Potassium", 1.0, 10.0, 4.5)
    st.caption("Normal Range: 3.5 - 5.0 mEq/L")

    hemoglobin = st.number_input("Hemoglobin", 1.0, 20.0, 14.0)
    st.caption("Normal Range: 12 - 16 g/dL")

    albumin = st.number_input("Albumin", 0.0, 5.0, 4.0)
    st.caption("Normal Range: 3.5 - 5.0 g/dL")
# ================= METRICS =================
st.markdown(
    "<h2 style='color:white;'>📊 Health Metrics</h2>",
    unsafe_allow_html=True
)

m1, m2, m3, m4 = st.columns(4)

cards = [
    ("Blood Pressure", bp),
    ("Creatinine", creatinine),
    ("Blood Urea", urea),
    ("Hemoglobin", hemoglobin)
]

for col, (title, value) in zip([m1,m2,m3,m4], cards):
    with col:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>{title}</h3>
            <h2>{value}</h2>
        </div>
        """, unsafe_allow_html=True)

# ================= ANALYSIS =================
if st.button("🔍 Analyze Report"):

    score = 0

    if creatinine > 1.3:
        score += 25
    if urea > 45:
        score += 20
    if bp > 140:
        score += 15
    if hemoglobin < 12:
        score += 15
    if sodium < 135:
        score += 10
    if potassium > 5:
        score += 15

    score = min(score, 100)

    if score >= 70:
        risk = "HIGH RISK"
        st.error(f"⚠️ HIGH RISK ({score}%)")
    elif score >= 40:
        risk = "MODERATE RISK"
        st.warning(f"🟠 MODERATE RISK ({score}%)")
    else:
        risk = "LOW RISK"
        st.success(f"🟢 LOW RISK ({score}%)")

    st.markdown(f"""
    <div class="result-card">
        <h2>Medical Summary</h2>
        <hr>
        <p><b>Disease:</b> {disease}</p>
        <p><b>Risk Score:</b> {score}%</p>
        <p><b>Assessment:</b> {risk}</p>
    </div>
    """, unsafe_allow_html=True)