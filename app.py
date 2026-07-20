import streamlit as st

st.set_page_config(
    page_title="PaddyScan - Klasifikasi Penyakit Daun Padi",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Global CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Hide default streamlit chrome */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* Hide default Streamlit page navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}            

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d2b1a 0%, #1a4a2e 100%);
    border-right: 1px solid #2d6a4f;
}
[data-testid="stSidebar"] * {
    color: #e8f5e9 !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 15px !important;
    font-weight: 500 !important;
    padding: 8px 0 !important;
    cursor: pointer !important;
}
[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p {
    font-size: 11px !important;
    color: #81c784 !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 600 !important;
    margin-bottom: 8px !important;
}

/* Main background */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    background-color: #f8faf8;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 20px 0 30px 0; text-align: center;">
        <div style="font-size: 42px; margin-bottom: 8px;">🌾</div>
        <div style="font-size: 20px; font-weight: 800; color: #a5d6a7; letter-spacing: -0.5px;">PaddyScan</div>
        <div style="font-size: 11px; color: #66bb6a; letter-spacing: 1px; margin-top: 4px;">DISEASE CLASSIFICATION AI</div>
    </div>
    <hr style="border: none; border-top: 1px solid #2d6a4f; margin: 0 0 20px 0;">
    """, unsafe_allow_html=True)

    page = st.radio(
        "NAVIGASI",
        ["🏠  Beranda", "🔬  Informasi Penyakit", "📷  Klasifikasi Penyakit"],
        label_visibility="visible"
    )

    st.markdown("""
    <div style="position: fixed; bottom: 30px; left: 0; width: 250px; padding: 0 20px; box-sizing: border-box;">
        <div style="font-size: 11px; color: #4caf50; text-align: center; letter-spacing: 0.5px;">
            Model: ConvNeXt-Tiny<br>
            <span style="color: #81c784;">Akurasi: 85.98%</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Page Router ──────────────────────────────────────────────────────────────
if "Beranda" in page:
    from pages.home import render
    render()
elif "Informasi" in page:
    from pages.info_penyakit import render
    render()
elif "Klasifikasi" in page:
    from pages.klasifikasi import render
    render()
