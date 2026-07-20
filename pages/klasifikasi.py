import streamlit as st
import torch
import torch.nn as nn
import timm
from torchvision import transforms
from PIL import Image
import numpy as np
import os
import gdown

MODEL_FILENAME = "convnext-tiny2(BS: 32, Epoch: 50, lr: 0.00005, DO: 0.5).pth"
MODEL_PATH = MODEL_FILENAME
GOOGLE_DRIVE_FILE_ID =  "1JTIflHpW6fO37R2uhaDc0RYHkizhF4SV"

# ── Class Labels ─────────────────────────────────────────────────────────────
CLASS_NAMES = ["BrownSpot", "Healthy", "Hispa", "LeafBlast"]

CLASS_META = {
    "BrownSpot":  {"label": "Brown Spot",  "emoji": "🟤", "color": "#f9a825", "bg": "#fff8e1", "border": "#ffe082"},
    "Healthy":    {"label": "Daun Sehat",   "emoji": "✅", "color": "#2e7d32", "bg": "#e8f5e9", "border": "#a5d6a7"},
    "Hispa":      {"label": "Hispa",        "emoji": "🐛", "color": "#c2185b", "bg": "#fce4ec", "border": "#f48fb1"},
    "LeafBlast":  {"label": "Leaf Blast",   "emoji": "💨", "color": "#512da8", "bg": "#ede7f6", "border": "#b39ddb"},
}

# ── Model Loader ──────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    # Buat folder models jika belum ada
    if not os.path.exists(MODEL_FILENAME):
        os.makedirs(MODEL_FILENAME)

    # Download jika file belum ada
    if not os.path.exists(MODEL_PATH):
        with st.spinner("⏳ Mengunduh model AI (sekitar 100MB), harap tunggu..."):
            url = f"https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}"
            try:
                gdown.download(url, MODEL_PATH, quiet=False)
            except Exception as e:
                st.error(f"Gagal mengunduh model: {e}")
                st.stop()
        st.success("✅ Model berhasil diunduh!")

    # Load model (sama seperti kode aslimu)
    model = timm.create_model("convnext_tiny", pretrained=False)
    in_features = model.head.fc.in_features
    model.head.fc = nn.Sequential(
        nn.Dropout(p=0.5),
        nn.Linear(in_features, 4)
    )
    state = torch.load(MODEL_PATH, map_location=torch.device("cpu"))
    model.load_state_dict(state)
    model.eval()
    return model

# ── Transforms ────────────────────────────────────────────────────────────────
def get_transform():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        ),
    ])

# ── Inference ─────────────────────────────────────────────────────────────────
def predict(model, image: Image.Image):
    tf = get_transform()
    tensor = tf(image.convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        logits = model(tensor)
        probs  = torch.softmax(logits, dim=1).squeeze().numpy()
    pred_idx   = int(np.argmax(probs))
    pred_class = CLASS_NAMES[pred_idx]
    return pred_class, probs


# ── Page ──────────────────────────────────────────────────────────────────────
def render():
    st.markdown("""
    <style>
    .page-hero {
        background: linear-gradient(135deg, #0d2b1a 0%, #1b5e20 100%);
        border-radius: 18px;
        padding: 44px 48px;
        margin-bottom: 36px;
        color: white;
    }
    .page-hero-eyebrow {
        font-size: 11px; font-weight: 700; letter-spacing: 2.5px;
        color: #a5d6a7; text-transform: uppercase; margin-bottom: 12px;
    }
    .page-hero-title {
        font-size: 38px; font-weight: 800; color: #ffffff;
        letter-spacing: -1px; margin-bottom: 12px; line-height: 1.15;
    }
    .page-hero-desc { font-size: 15px; color: #c8e6c9; line-height: 1.7; max-width: 500px; }

    .upload-zone {
        background: #ffffff;
        border: 2px dashed #a5d6a7;
        border-radius: 18px;
        padding: 40px 32px;
        text-align: center;
        transition: all 0.2s ease;
        margin-bottom: 20px;
    }
    .upload-zone:hover { border-color: #2e7d32; background: #f8fdf8; }
    .upload-title { font-size: 17px; font-weight: 700; color: #1b2e1b; margin-bottom: 6px; }
    .upload-sub   { font-size: 13px; color: #7a9a7a; }

    .step-row {
        display: flex; gap: 12px; margin-bottom: 28px; flex-wrap: wrap;
    }
    .step-item {
        display: flex; align-items: center; gap: 10px;
        background: #f0f7f0; border-radius: 100px;
        padding: 8px 16px; font-size: 13px; color: #2e7d32; font-weight: 600;
    }
    .step-num {
        width: 22px; height: 22px; border-radius: 50%;
        background: #2e7d32; color: white;
        display: flex; align-items: center; justify-content: center;
        font-size: 11px; font-weight: 800; flex-shrink: 0;
    }

    /* Result card */
    .result-outer {
        background: #ffffff;
        border: 1px solid #e0ece0;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        margin-top: 8px;
    }
    .result-header {
        padding: 24px 28px 20px;
        border-bottom: 1px solid #f0f0f0;
    }
    .result-label {
        font-size: 11px; font-weight: 700; letter-spacing: 2px;
        text-transform: uppercase; color: #7a9a7a; margin-bottom: 8px;
    }
    .result-disease {
        font-size: 30px; font-weight: 800;
        letter-spacing: -0.8px; line-height: 1;
        margin-bottom: 6px;
    }
    .result-confidence {
        font-size: 14px; color: #4a5e4a; font-weight: 500;
    }
    .result-confidence span { font-weight: 800; }
    .result-body { padding: 24px 28px; }
    .bar-row { margin-bottom: 14px; }
    .bar-label {
        display: flex; justify-content: space-between;
        font-size: 13px; color: #4a4a4a; font-weight: 500;
        margin-bottom: 5px;
    }
    .bar-track {
        height: 8px; background: #f0f0f0;
        border-radius: 100px; overflow: hidden;
    }
    .bar-fill { height: 100%; border-radius: 100px; transition: width 0.6s ease; }

    .tip-box {
        background: #f8fdf8; border: 1px solid #c8e6c9;
        border-radius: 14px; padding: 18px 20px;
        font-size: 13px; color: #2e7d32; line-height: 1.6; margin-top: 20px;
    }
    .tip-box strong { font-weight: 700; }

    .warning-box {
        background: #fff8e1; border: 1px solid #ffe082;
        border-radius: 14px; padding: 16px 20px;
        font-size: 13px; color: #5d4037; line-height: 1.6; margin-top: 16px;
    }
    </style>

    <div class="page-hero">
        <div class="page-hero-eyebrow">📷 AI Diagnosis</div>
        <div class="page-hero-title">Klasifikasi Penyakit Daun Padi</div>
        <div class="page-hero-desc">
            Unggah gambar daun padi, klik <strong>Mulai Scanning</strong>, 
            dan sistem akan menganalisis kondisi daun secara otomatis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Step indicator ────────────────────────────────────────────────────────
    st.markdown("""
    <div class="step-row">
        <div class="step-item"><div class="step-num">1</div> Unggah gambar daun padi</div>
        <div class="step-item"><div class="step-num">2</div> Klik "Mulai Scanning"</div>
        <div class="step-item"><div class="step-num">3</div> Lihat hasil diagnosis</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Layout: upload kiri | hasil kanan ────────────────────────────────────
    col_left, col_right = st.columns([1, 1.1], gap="large")

    with col_left:
        # Model path input
        # model_path = st.text_input(
        #     "Path ke file model (.pth)",
        #     value="best_model.pth",
        #     help="Masukkan path lengkap ke file model PyTorch kamu"
        # )

        uploaded = st.file_uploader(
            "Upload gambar daun padi",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )

        if uploaded:
            img = Image.open(uploaded).convert("RGB")
            st.image(img, caption="Gambar yang diupload", use_container_width=True)

            scan_btn = st.button(
                "🔍  Start Scanning",
                use_container_width=True,
                type="primary"
            )
        else:
            st.markdown("""
            <div class="upload-zone">
                <div style="font-size:48px; margin-bottom:12px;">🌿</div>
                <div class="upload-title">Drag & drop atau klik untuk upload</div>
                <div class="upload-sub">Format yang didukung: JPG, JPEG, PNG</div>
            </div>
            """, unsafe_allow_html=True)
            scan_btn = False

    with col_right:
        if uploaded and scan_btn:
            with st.spinner("Menganalisis gambar..."):
                try:
                    model = load_model()
                    pred_class, probs = predict(model, img)
                    meta = CLASS_META[pred_class]

                    # Result card header
                    st.markdown(f"""
                    <div class="result-outer">
                        <div class="result-header"
                             style="background:{meta['bg']}; border-bottom-color:{meta['border']};">
                            <div class="result-label">Hasil Diagnosis</div>
                            <div class="result-disease" style="color:{meta['color']};">
                                {meta['emoji']} {meta['label']}
                            </div>
                            <div class="result-confidence">
                                Confidence score: <span style="color:{meta['color']};">{probs[CLASS_NAMES.index(pred_class)]:.1%}</span>
                            </div>
                        </div>
                        <div class="result-body">
                            <div style="font-size:12px; font-weight:700; letter-spacing:1.5px;
                                        text-transform:uppercase; color:#7a9a7a; margin-bottom:16px;">
                                Distribusi Probabilitas
                            </div>
                    """, unsafe_allow_html=True)

                    # Probability bars for each class
                    bar_colors = {
                        "BrownSpot": "#f9a825",
                        "Healthy":   "#2e7d32",
                        "Hispa":     "#c2185b",
                        "LeafBlast": "#512da8",
                    }
                    bar_rows = ""
                    sorted_idx = np.argsort(probs)[::-1]
                    for idx in sorted_idx:
                        cn    = CLASS_NAMES[idx]
                        prob  = probs[idx]
                        color = bar_colors[cn]
                        label = CLASS_META[cn]["label"]
                        bold  = "font-weight:800;" if cn == pred_class else ""
                        bar_rows += f"""
                        <div class="bar-row">
                            <div class="bar-label">
                                <span style="{bold}">{CLASS_META[cn]['emoji']} {label}</span>
                                <span style="{bold} color:{color};">{prob:.1%}</span>
                            </div>
                            <div class="bar-track">
                                <div class="bar-fill" style="width:{prob*100:.1f}%; background:{color};"></div>
                            </div>
                        </div>
                        """

                    st.markdown(bar_rows + "</div></div>", unsafe_allow_html=True)

                    # Extra tips
                    if pred_class == "Healthy":
                        st.markdown("""
                        <div class="tip-box">
                            ✅ <strong>Daun padi dalam kondisi sehat!</strong><br>
                            Pertahankan kondisi ini dengan pemupukan berimbang dan 
                            pemantauan rutin minimal dua kali seminggu.
                        </div>
                        """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan saat memproses: {e}")

        elif not uploaded:
            st.markdown("""
            <div style="background:#f8faf8; border:1px solid #e0ece0; border-radius:18px;
                        padding:60px 32px; text-align:center; color:#90a890; margin-top: 0px;">
                <div style="font-size:48px; margin-bottom:16px; opacity:0.5;">🔬</div>
                <div style="font-size:16px; font-weight:600; margin-bottom:8px; color:#4a6a4a;">
                    Hasil akan tampil di sini
                </div>
                <div style="font-size:13px; line-height:1.6;">
                    Upload gambar daun padi terlebih dahulu<br>
                    kemudian klik <strong>Start Scanning</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)
