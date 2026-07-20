import streamlit as st
import base64
from pathlib import Path
 
# ── Embedded sample images (base64) ──────────────────────────────────────────
def _b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()
 
def _img_tag(b64: str, alt: str) -> str:
    return f'<img src="data:image/jpeg;base64,{b64}" alt="{alt}" style="width:100%; height:180px; object-fit:cover; border-radius:10px; margin-bottom:16px; display:block;">'
 
# Coba load dari folder assets/, fallback ke path upload
def _load_img(filename: str, fallback_path: str) -> str:
    asset = Path("assets") / filename
    if asset.exists():
        return _b64(str(asset))
    return _b64(fallback_path)
 
IMAGES = {
    "Brown Spot":  _load_img("brownspot.jpg",  "/mnt/user-data/uploads/brownspot.jpg"),
    "Hispa":       _load_img("hispa.jpg",       "/mnt/user-data/uploads/hispa.jpg"),
    "Leaf Blast":  _load_img("leafblast.jpg",   "/mnt/user-data/uploads/leafblast.jpg"),
    "Healthy":     _load_img("healthy.jpg",     "/mnt/user-data/uploads/healthy.jpg"),
}
 
DISEASES = {
    "Healthy": {
        "emoji": "✅",
        "latin": "—",
        "color_bg": "#e8f5e9",
        "color_border": "#a5d6a7",
        "color_text": "#1b5e20",
        "severity": "Tidak ada",
        "severity_color": "#2e7d32",
        "deskripsi": (
            "Daun padi dalam kondisi sehat menunjukkan pertumbuhan yang optimal dan "
            "bebas dari serangan penyakit maupun hama. Tanaman padi yang sehat memiliki "
            "daun berwarna hijau segar, tegak, dan tidak menunjukkan bercak, perubahan "
            "warna abnormal, atau kerusakan jaringan. Kondisi ini mencerminkan pengelolaan "
            "lahan yang baik dan lingkungan tumbuh yang mendukung."
        ),
        "gejala": [
            "Daun berwarna hijau segar dan merata tanpa bercak abnormal",
            "Permukaan daun bersih, tidak ada goresan atau robekan",
            "Pertumbuhan tanaman tegak dan proporsional sesuai umur",
            "Tidak ditemukan bekas gigitan hama atau gejala infeksi jamur",
            "Warna daun seragam dari pangkal hingga ujung",
        ],
        "penyebab": [
            "Pengelolaan nutrisi dan pemupukan yang tepat",
            "Sistem irigasi yang terkontrol dengan baik",
            "Pengendalian hama dan penyakit yang dilakukan secara preventif",
            "Penggunaan benih unggul bersertifikat dari varietas tahan penyakit",
        ],
    },
    "Brown Spot": {
        "emoji": "🟤",
        "latin": "Helminthosporium oryzae",
        "color_bg": "#fff8e1",
        "color_border": "#ffe082",
        "color_text": "#5d4037",
        "severity": "Sedang – Tinggi",
        "severity_color": "#e65100",
        "deskripsi": (
            "Brown Spot (bercak cokelat) merupakan salah satu penyakit padi yang paling umum "
            "ditemukan di berbagai wilayah penghasil padi. Penyakit ini disebabkan oleh jamur "
            "Helminthosporium oryzae dan dapat menyebabkan penurunan hasil panen hingga 45% "
            "jika tidak ditangani segera."
        ),
        "gejala": [
            "Bercak oval kecil berwarna cokelat atau kekuningan pada permukaan daun",
            "Tepi bercak berwarna kuning atau oranye (halo effect)",
            "Bercak dapat bergabung dan menyebabkan daun mengering",
            "Pada serangan berat, seluruh daun dapat berwarna cokelat dan mati",
            "Bercak juga dapat muncul pada malai dan biji padi",
        ],
        "penyebab": [
            "Kondisi tanah dengan kandungan hara rendah (terutama Kalium dan Silika)",
            "Cuaca lembab dengan suhu 25–30°C",
            "Kelembapan udara tinggi di atas 80%",
            "Tanaman padi yang stres akibat kekurangan air",
        ],
    },
    "Hispa": {
        "emoji": "🐛",
        "latin": "Dicladispa armigera",
        "color_bg": "#fce4ec",
        "color_border": "#f48fb1",
        "color_text": "#880e4f",
        "severity": "Sedang",
        "severity_color": "#c62828",
        "deskripsi": (
            "Hispa (Dicladispa armigera) adalah serangan hama kumbang kecil berwarna biru-hitam "
            "dengan tubuh berduri. Larva dan imago menyerang daun padi dengan cara menggerek "
            "jaringan daun dari dalam, meninggalkan pola khas berwarna putih memanjang. "
            "Serangan dapat menyebabkan penurunan produksi hingga 10–30%."
        ),
        "gejala": [
            "Goresan putih memanjang sejajar tulang daun (akibat larva yang mengerek)",
            "Daun tampak keputihan atau transparan pada bagian yang terserang",
            "Pada serangan berat seluruh permukaan daun berwarna putih dan kering",
            "Tampak bekas gigitan di pinggiran daun (akibat imago dewasa)",
            "Pertumbuhan tanaman terhambat pada serangan stadium awal",
        ],
        "penyebab": [
            "Kepadatan populasi hama Dicladispa armigera yang tinggi",
            "Musim kemarau dengan suhu tinggi yang mendukung perkembangan hama",
            "Tanaman padi muda yang masih dalam fase vegetatif (rentan serangan)",
            "Penggunaan insektisida yang tidak tepat waktu dan dosis",
        ],
    },
    "Leaf Blast": {
        "emoji": "💨",
        "latin": "Pyricularia oryzae",
        "color_bg": "#ede7f6",
        "color_border": "#b39ddb",
        "color_text": "#311b92",
        "severity": "Tinggi – Sangat Tinggi",
        "severity_color": "#b71c1c",
        "deskripsi": (
            "Leaf Blast adalah penyakit paling merusak pada tanaman padi di seluruh dunia, "
            "disebabkan oleh jamur Pyricularia oryzae. Penyakit ini dapat menyerang pada "
            "semua fase pertumbuhan padi dan mampu menghancurkan seluruh hasil panen "
            "jika kondisi lingkungan mendukung perkembangannya. Di Indonesia, penyakit ini "
            "menjadi ancaman serius bagi produktivitas padi nasional."
        ),
        "gejala": [
            "Bercak berbentuk belah ketupat (diamond shape) dengan ujung runcing",
            "Bagian tengah bercak berwarna abu-abu atau putih, tepi berwarna cokelat",
            "Di sekitar bercak terdapat halo berwarna kuning",
            "Pada serangan berat, bercak-bercak bergabung dan daun mati",
            "Leher malai berwarna kehitaman dan patah (neck blast) pada fase berbunga",
        ],
        "penyebab": [
            "Suhu rendah 20–25°C dengan embun pagi yang tebal",
            "Kelembapan udara sangat tinggi (> 90%) dan cuaca berawan",
            "Pemupukan Nitrogen berlebihan yang mempercepat penyebaran spora",
            "Penggunaan varietas padi yang tidak tahan blast",
            "Angin yang membantu penyebaran spora jamur ke area yang lebih luas",
        ],
    },
    "Healthy": {
        "emoji": "✅",
        "latin": "—",
        "color_bg": "#e8f5e9",
        "color_border": "#a5d6a7",
        "color_text": "#1b5e20",
        "severity": "Tidak ada",
        "severity_color": "#2e7d32",
        "deskripsi": (
            "Daun padi dalam kondisi sehat menunjukkan pertumbuhan yang optimal dan "
            "bebas dari serangan penyakit maupun hama. Tanaman padi yang sehat memiliki "
            "daun berwarna hijau segar, tegak, dan tidak menunjukkan bercak, perubahan "
            "warna abnormal, atau kerusakan jaringan. Kondisi ini mencerminkan pengelolaan "
            "lahan yang baik dan lingkungan tumbuh yang mendukung."
        ),
        "gejala": [
            "Daun berwarna hijau segar dan merata tanpa bercak abnormal",
            "Permukaan daun bersih, tidak ada goresan atau robekan",
            "Pertumbuhan tanaman tegak dan proporsional sesuai umur",
            "Tidak ditemukan bekas gigitan hama atau gejala infeksi jamur",
            "Warna daun seragam dari pangkal hingga ujung",
        ],
        "penyebab": [
            "Pengelolaan nutrisi dan pemupukan yang tepat",
            "Sistem irigasi yang terkontrol dengan baik",
            "Pengendalian hama dan penyakit yang dilakukan secara preventif",
            "Penggunaan benih unggul bersertifikat dari varietas tahan penyakit",
        ],
    },
}
 
 
def render():
    st.markdown("""
    <style>
    .page-hero {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%);
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
    .page-hero-desc { font-size: 15px; color: #c8e6c9; line-height: 1.7; max-width: 520px; }
 
    .disease-card {
        border-radius: 18px;
        padding: 32px;
        margin-bottom: 24px;
        border: 1.5px solid;
    }
    .disease-header {
        display: flex; align-items: center; gap: 16px; margin-bottom: 20px;
    }
    .disease-emoji { font-size: 36px; }
    .disease-name {
        font-size: 24px; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 2px;
    }
    .disease-latin { font-size: 13px; font-style: italic; opacity: 0.6; }
    .severity-badge {
        display: inline-block; border-radius: 100px; padding: 4px 14px;
        font-size: 12px; font-weight: 700; color: white; margin-left: auto;
    }
    .disease-desc {
        font-size: 14.5px; line-height: 1.75; margin-bottom: 24px; opacity: 0.85;
    }
    .card-body {
        display: grid; grid-template-columns: 220px 1fr 1fr; gap: 20px; align-items: start;
    }
    .sample-img-wrap {
        border-radius: 12px; overflow: hidden;
    }
    .info-box {
        background: rgba(255,255,255,0.55);
        border-radius: 12px; padding: 20px 18px;
        border: 1px solid rgba(255,255,255,0.7);
    }
    .info-box-title {
        font-size: 11px; font-weight: 700; letter-spacing: 1.5px;
        text-transform: uppercase; margin-bottom: 12px; opacity: 0.65;
    }
    .info-item {
        font-size: 13px; line-height: 1.6; margin-bottom: 7px;
        padding-left: 14px; position: relative; opacity: 0.85;
    }
    .info-item::before { content: '›'; position: absolute; left: 0; font-weight: 700; }
    </style>
 
    <div class="page-hero">
        <div class="page-hero-eyebrow">🔬 Ensiklopedia</div>
        <div class="page-hero-title">Informasi Penyakit Daun Padi</div>
        <div class="page-hero-desc">
            Pelajari karakteristik, gejala, dan faktor penyebab 
            empat kondisi daun padi yang dikenali oleh sistem RiceGuard.
        </div>
    </div>
    """, unsafe_allow_html=True)
 
    for name, info in DISEASES.items():
        gejala_html    = "".join(f'<div class="info-item">{g}</div>' for g in info["gejala"])
        penyebab_html  = "".join(f'<div class="info-item">{p}</div>' for p in info["penyebab"])
        img_tag        = _img_tag(IMAGES[name], f"Sampel daun {name}")
 
        st.markdown(f"""
        <div class="disease-card"
             style="background:{info['color_bg']};
                    border-color:{info['color_border']};
                    color:{info['color_text']};">
            <div class="disease-header">
                <span class="disease-emoji">{info['emoji']}</span>
                <div>
                    <div class="disease-name">{name}</div>
                    <div class="disease-latin">{info['latin']}</div>
                </div>
                <span class="severity-badge" style="background:{info['severity_color']};">
                    Keparahan: {info['severity']}
                </span>
            </div>
            <div class="disease-desc">{info['deskripsi']}</div>
            <div class="card-body">
                <div class="sample-img-wrap">
                    <div class="info-box-title" style="margin-bottom:8px;">Foto Sampel</div>
                    {img_tag}
                </div>
                <div class="info-box">
                    <div class="info-box-title">Gejala Utama</div>
                    {gejala_html}
                </div>
                <div class="info-box">
                    <div class="info-box-title">Faktor Penyebab</div>
                    {penyebab_html}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
 
    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)