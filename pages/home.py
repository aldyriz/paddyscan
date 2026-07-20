import streamlit as st

def render():
    # ── Hero Section ─────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    .hero-wrapper {
        background: linear-gradient(135deg, #0d2b1a 0%, #1b5e20 50%, #2e7d32 100%);
        border-radius: 20px;
        padding: 64px 56px;
        position: relative;
        overflow: hidden;
        margin-bottom: 40px;
    }
    .hero-wrapper::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 280px; height: 280px;
        background: rgba(129,199,132,0.08);
        border-radius: 50%;
    }
    .hero-wrapper::after {
        content: '';
        position: absolute;
        bottom: -80px; left: 40%;
        width: 200px; height: 200px;
        background: rgba(76,175,80,0.06);
        border-radius: 50%;
    }
    .hero-eyebrow {
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2.5px;
        color: #69f0ae;
        text-transform: uppercase;
        margin-bottom: 18px;
    }
    .hero-title {
        font-size: 48px;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.15;
        letter-spacing: -1.5px;
        margin-bottom: 20px;
    }
    .hero-title span {
        color: #69f0ae;
    }
    .hero-subtitle {
        font-size: 17px;
        color: #a5d6a7;
        line-height: 1.7;
        max-width: 560px;
        margin-bottom: 36px;
        font-weight: 400;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(105, 240, 174, 0.12);
        border: 1px solid rgba(105, 240, 174, 0.3);
        border-radius: 100px;
        padding: 8px 18px;
        font-size: 13px;
        color: #69f0ae;
        font-weight: 600;
        margin-right: 10px;
        margin-bottom: 8px;
        display: inline-block;
    }
    .stat-row {
        display: flex;
        gap: 24px;
        margin-top: 40px;
        flex-wrap: wrap;
    }
    .stat-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 14px;
        padding: 20px 28px;
        flex: 1;
        min-width: 140px;
        backdrop-filter: blur(10px);
    }
    .stat-num {
        font-size: 32px;
        font-weight: 800;
        color: #69f0ae;
        letter-spacing: -1px;
        line-height: 1;
        margin-bottom: 4px;
    }
    .stat-label {
        font-size: 12px;
        color: #a5d6a7;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* About section */
    .section-label {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2.5px;
        color: #2e7d32;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    .section-title {
        font-size: 30px;
        font-weight: 800;
        color: #2e7d32;
        letter-spacing: -0.8px;
        margin-bottom: 14px;
        line-height: 1.2;
    }
    .section-body {
        font-size: 15px;
        color: #2e7d32;
        line-height: 1.8;
        margin-bottom: 0;
    }

    /* Feature cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 28px;
    }
    .feature-card {
        background: #ffffff;
        border: 1px solid #e8f5e9;
        border-radius: 16px;
        padding: 28px 24px;
        transition: all 0.2s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .feature-icon {
        font-size: 28px;
        margin-bottom: 14px;
        display: block;
    }
    .feature-title {
        font-size: 15px;
        font-weight: 700;
        color: #1b2e1b;
        margin-bottom: 8px;
    }
    .feature-desc {
        font-size: 13px;
        color: #6b7c6b;
        line-height: 1.65;
    }

    /* Tech stack */
    .tech-wrapper {
        background: #ffffff;
        border: 1px solid #e8f5e9;
        border-radius: 20px;
        padding: 40px 44px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    }
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-top: 28px;
    }
    .tech-item {
        background: #f8faf8;
        border: 1px solid #e0ece0;
        border-radius: 14px;
        padding: 20px 16px;
        text-align: center;
    }
    .tech-emoji {
        font-size: 26px;
        display: block;
        margin-bottom: 10px;
    }
    .tech-name {
        font-size: 14px;
        font-weight: 700;
        color: #1b2e1b;
        margin-bottom: 4px;
    }
    .tech-role {
        font-size: 11px;
        color: #7a9a7a;
        font-weight: 500;
    }

    /* Disease preview */
    .disease-chip {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #e8f5e9;
        border: 1px solid #c8e6c9;
        border-radius: 100px;
        padding: 7px 16px;
        font-size: 13px;
        font-weight: 600;
        color: #1b5e20;
        margin: 5px 5px 5px 0;
    }
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #c8e6c9, transparent);
        margin: 48px 0;
        border: none;
    }
    </style>

    <!-- HERO -->
    <div class="hero-wrapper">
        <div class="hero-eyebrow">🌾 Sistem Deteksi Cerdas</div>
        <div class="hero-title">
            Identifikasi Penyakit<br>Daun Padi dengan <span>AI</span>
        </div>
        <div class="hero-subtitle">
            PaddyScan menggunakan arsitektur deep learning ConvNeXt-Tiny untuk mendeteksi 
            penyakit daun padi secara otomatis dari gambar. Cukup unggah foto daun, 
            dan sistem akan mengidentifikasi kondisinya dalam hitungan detik.
        </div>
        <div>
            <span class="hero-badge">✦ Brown Spot</span>
            <span class="hero-badge">✦ Hispa</span>
            <span class="hero-badge">✦ Leaf Blast</span>
            <span class="hero-badge">✦ Healthy</span>
        </div>
        <div class="stat-row">
            <div class="stat-card">
                <div class="stat-num">85.98%</div>
                <div class="stat-label">Akurasi Model</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">4</div>
                <div class="stat-label">Kelas Penyakit</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">224px</div>
                <div class="stat-label">Resolusi Input</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">50</div>
                <div class="stat-label">Epoch Training</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── About Section ─────────────────────────────────────────────────────────
    col_about, col_features = st.columns([1, 1.4], gap="large")

    with col_about:
        st.markdown("""
        <div class="section-label">Tentang Aplikasi</div>
        <div class="section-title">Mengapa PaddyScan?</div>
        <div class="section-body">
            Padi adalah komoditas pangan utama Indonesia. Penyakit pada daun padi 
            dapat menurunkan hasil panen secara drastis jika tidak terdeteksi sejak dini.
            <br><br>
            PaddyScan hadir sebagai solusi berbasis kecerdasan buatan yang memudahkan 
            petani dan peneliti dalam mengidentifikasi kondisi tanaman padi melalui 
            analisis gambar daun secara otomatis dan akurat.
            <br><br>
            Dibangun sebagai bagian dari penelitian skripsi menggunakan arsitektur 
            <strong>ConvNeXt-Tiny</strong> dengan teknik <em>transfer learning</em> 
            dari bobot ImageNet, model ini mampu membedakan empat kondisi daun padi 
            dengan akurasi tinggi.
        </div>
        """, unsafe_allow_html=True)

    with col_features:
        st.markdown("""
        <div class="section-label">Fitur Utama</div>
        <div class="section-title">Apa yang bisa dilakukan?</div>
        <div class="feature-grid">
            <div class="feature-card">
                <span class="feature-icon">📷</span>
                <div class="feature-title">Upload & Scan</div>
                <div class="feature-desc">Unggah gambar daun padi dan dapatkan hasil diagnosa instan.</div>
            </div>
            <div class="feature-card">
                <span class="feature-icon">🎯</span>
                <div class="feature-title">Confidence Score</div>
                <div class="feature-desc">Setiap prediksi disertai skor kepercayaan untuk tiap kelas.</div>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📖</span>
                <div class="feature-title">Info Penyakit</div>
                <div class="feature-desc">Pelajari karakteristik dan cara penanganan tiap penyakit.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # ── Tech Stack Section ────────────────────────────────────────────────────
    st.markdown("""
    <div class="tech-wrapper">
        <div class="section-label">Teknologi</div>
        <div class="section-title">Dibangun dengan teknologi modern</div>
        <div class="tech-grid">
            <div class="tech-item">
                <span class="tech-emoji">🔥</span>
                <div class="tech-name">PyTorch</div>
                <div class="tech-role">Deep Learning Framework</div>
            </div>
            <div class="tech-item">
                <span class="tech-emoji">🧠</span>
                <div class="tech-name">ConvNeXt-Tiny</div>
                <div class="tech-role">Arsitektur Model</div>
            </div>
            <div class="tech-item">
                <span class="tech-emoji">⚡</span>
                <div class="tech-name">Streamlit</div>
                <div class="tech-role">Web Framework</div>
            </div>
            <div class="tech-item">
                <span class="tech-emoji">🖼️</span>
                <div class="tech-name">Torchvision</div>
                <div class="tech-role">Image Processing</div>
            </div>
            <div class="tech-item">
                <span class="tech-emoji">📦</span>
                <div class="tech-name">timm</div>
                <div class="tech-role">Pretrained Models</div>
            </div>
            <div class="tech-item">
                <span class="tech-emoji">🐍</span>
                <div class="tech-name">Python 3.10</div>
                <div class="tech-role">Programming Language</div>
            </div>
            <div class="tech-item">
                <span class="tech-emoji">🔢</span>
                <div class="tech-name">NumPy</div>
                <div class="tech-role">Numerical Computing</div>
            </div>
            <div class="tech-item">
                <span class="tech-emoji">🖼</span>
                <div class="tech-name">Pillow</div>
                <div class="tech-role">Image I/O</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align: center; padding: 24px 0; color: #90a890; font-size: 13px;">
        PaddyScan &nbsp;·&nbsp; Tugas Akhir Skripsi &nbsp;·&nbsp; 
        Klasifikasi Penyakit Daun Padi Menggunakan ConvNeXt-Tiny
    </div>
    """, unsafe_allow_html=True)
