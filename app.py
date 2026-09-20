import streamlit as st
import datetime

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Portali | 38-modda",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. "Oltin Gologramma" - Hukumat Darajasidagi Premium CSS Dizayn (Sof CSS3)
st.markdown("""
    <style>
    /* 1. Asosiy Fon - Rasmiy va Chuqur (Deep Dark Blue/Black) */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0d1425 0%, #04070d 100%) !important;
        background-attachment: fixed;
        overflow-x: hidden;
    }

    /* 2. Gologrammalar Konteyneri */
    .hologram-container {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: 0;
        pointer-events: none; /* Kursorga xalaqit bermaydi */
        overflow: hidden;
    }

    /* 3. Gologramma elementlarining umumiy uslubi */
    .holo-symbol {
        position: absolute;
        font-family: "Times New Roman", Times, serif;
        /* Emojilarni tilla rangli gologrammaga aylantirish uchun maxsus filtr */
        filter: grayscale(100%) sepia(100%) hue-rotate(10deg) saturate(500%) brightness(1.2) opacity(0.08);
        text-shadow: 0 0 20px rgba(212, 175, 55, 0.5), 0 0 40px rgba(212, 175, 55, 0.3);
        animation: rotateHolo linear infinite, flickerHolo 5s infinite alternate;
    }

    /* O'lchamlari va joylashuvi */
    .holo-scales { /* Tarozi */
        font-size: 70vh;
        top: -10%; left: -15%;
        animation-duration: 90s;
    }
    
    .holo-building { /* Bino/Sud */
        font-size: 80vh;
        bottom: -20%; right: -10%;
        animation-duration: 120s;
        animation-direction: reverse;
        filter: grayscale(100%) sepia(100%) hue-rotate(10deg) saturate(500%) brightness(1.2) opacity(0.05);
    }

    .holo-paragraph { /* Paragraf belgisi */
        font-size: 100vh;
        top: 10%; left: 35%;
        color: #d4af37; /* Sof tilla rang */
        filter: opacity(0.03); /* Emojimasligi uchun oddiy xiralashtirish */
        animation-duration: 150s;
    }

    /* 4. Gologramma Harakatlari (Aylanish va Miltillash) */
    @keyframes rotateHolo {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.05); }
        100% { transform: rotate(360deg) scale(1); }
    }

    @keyframes flickerHolo {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% { opacity: 0.08; text-shadow: 0 0 20px rgba(212, 175, 55, 0.5); }
        20%, 24%, 55% { opacity: 0.02; text-shadow: none; }
    }

    /* --- PREMIUM SHISHA (GLASSMORPHISM) INTERFEYS --- */
    
    /* Yon panelni (Sidebar) moslashtirish */
    [data-testid="stSidebar"] {
        background: rgba(4, 7, 13, 0.85) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(212, 175, 55, 0.15); /* Yengil tilla hoshiya */
    }

    /* Asosiy bloklar (Konteynerlar) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(12, 18, 30, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(212, 175, 55, 0.25) !important; /* Tilla rang hoshiya */
        border-radius: 16px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), inset 0 0 15px rgba(212, 175, 55, 0.05) !important;
        transition: all 0.4s ease !important;
        position: relative;
        z-index: 10;
    }

    /* Konteyner ustiga sichqoncha borganda */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(212, 175, 55, 0.7) !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.9), inset 0 0 20px rgba(212, 175, 55, 0.15) !important;
        transform: translateY(-4px);
    }

    /* Matnlar va Sarlavhalarni Premium Oltin rangga o'tkazish */
    h1, h2, h3, h4 { color: #d4af37 !important; text-shadow: 0 2px 4px rgba(0,0,0,0.8); letter-spacing: 0.5px; }
    label, span, p, .stMarkdown { color: #e2e8f0 !important; }

    /* Checkbox (tasdiq belgilari) dizayni */
    div[data-baseweb="checkbox"] > div {
        background-color: transparent !important;
    }

    /* Oltin Tugmalar Dizayni */
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(135deg, #8a7322 0%, #d4af37 50%, #8a7322 100%) !important;
        color: #04070d !important; /* To'q fon uchun qora matn */
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 8px !important;
        border: 1px solid #ffdf73 !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover, .stDownloadButton>button:hover {
        background: linear-gradient(135deg, #ffd700 0%, #ffea70 50%, #ffd700 100%) !important;
        box-shadow: 0 6px 25px rgba(212, 175, 55, 0.6) !important;
        transform: translateY(-2px) scale(1.02);
    }
    </style>

    <!-- Gologramma elementlari -->
    <div class="hologram-container">
        <div class="holo-symbol holo-scales">⚖️</div>
        <div class="holo-symbol holo-building">🏛️</div>
        <div class="holo-symbol holo-paragraph">§</div>
    </div>
""", unsafe_allow_html=True)

# 3. Yon panel (Sidebar)
with st.sidebar:
    st.title("⚖️ LexiDraft Portal")
    st.info(
        "**38-modda toʻgʻrisida:**\n\n"
        "Oʻzbekiston Respublikasining Fuqarolik toʻgʻrisidagi Qonuniga muvofiq, "
        "iltimosnomalarga ilova qilinishi shart boʻlgan rasmiy hujjatlar roʻyxati."
    )
    st.divider()
    st.caption("Avtomatlashtirilgan huquqiy tahlil tizimi")

# 4. Asosiy sarlavha
st.title("⚖️ Fuqarolik Iltimosnomasi Portali")
st.caption("Oʻzbekiston Respublikasi Fuqarolik toʻgʻrisidagi Qonunining 38-moddasi asosida avtomatlashtirilgan tekshirish")
st.divider()

# 5. Ikki ustunli struktura
col1, col2 = st.columns([1.2, 0.8], gap="large")

with col1:
    # 1-Konteyner: Tartibni tanlash
    with st.container(border=True):
        st.subheader("1. Tartib va shartlarni tanlang")
        procedure = st.selectbox(
            "Iltimosnoma turi:",
            [
                "Umumiy tartibda qabul qilish yoki fuqarolikni tiklash",
                "Soddalashtirilgan tartibda qabul qilish",
                "Alohida tartibda qabul qilish"
            ]
        )

        with_child = False
        if procedure != "Alohida tartibda qabul qilish":
            with_child = st.checkbox("Iltimosnomada yosh bola (farzand) ko'rsatilganmi?")

    # Hujjatlar ro'yxatini shakllantirish
    docs_required = []
    if procedure == "Alohida tartibda qabul qilish":
        docs_required = [
            "Pasport yoki identifikatsiyalovchi karta (yashash guvohnomasi)"
        ]
    else:
        docs_required = [
            "Soʻrovnoma",
            "Pasport yoki identifikatsiyalovchi karta (yashash guvohnomasi)",
            "Nikoh tuzilganligi yoki nikoh bekor qilinganligi toʻgʻrisidagi guvohnoma",
            "Tirikchilikning qonuniy manbalari mavjudligini tasdiqlovchi hujjat"
        ]
        
        if with_child:
            docs_required.append(
                "Bolaning tugʻilganlik toʻgʻrisidagi guvohnomasi va yashash guvohnomasi (agar mavjud boʻlsa)"
            )
            
        if procedure == "Soddalashtirilgan tartibda qabul qilish":
            docs_required.extend([
                "Ariza beruvchining tugʻilganlik toʻgʻrisidagi guvohnomasi",
                "Oʻzbekiston Respublikasi hududida yashayotgan va Oʻzbekiston Respublikasining fuqarosi boʻlgan, nasl-nasab shajarasi boʻyicha toʻgʻri tutashgan oʻzidan oldingi qarindoshining pasporti (ID-kartasi) yoxud manfaatdor vazirlik/idoraning iltimosnomasi",
                "Sudlanganlik holati yoʻqligini yoki mavjudligini tasdiqlovchi hujjat"
            ])

    # 2-Konteyner: Hujjatlar ro'yxati
    with st.container(border=True):
        st.subheader("2. Hujjatlar nazorat roʻyxati")
        st.caption("Mavjud hujjatlarni belgilab chiqing:")

        completed_docs = []
        missing_docs = []

        for idx, doc in enumerate(docs_required, 1):
            status = st.checkbox(f"{doc}", key=f"doc_{idx}")
            if status:
                completed_docs.append(doc)
            else:
                missing_docs.append(doc)

with col2:
    total = len(docs_required)
    current = len(completed_docs)
    progress = current / total if total > 0 else 0

    # 3-Konteyner: Tahlil va Progress
    with st.container(border=True):
        st.subheader("📊 Tayyorgarlik holati")
        st.progress(progress)
        
        st.metric(
            label="Tayyor bo'lgan hujjatlar", 
            value=f"{int(progress * 100)}%", 
            delta=f"{current}/{total} ta hujjat"
        )

        if current == total:
            st.success("🎉 Barcha kerakli hujjatlar to'liq jamlandi! Topshirishga tayyor.")
        else:
            st.warning(f"⚠️ Yana {total - current} ta hujjat yetishmayapti.")

    # 4-Konteyner: Hisobot va Yuklab olish
    with st.container(border=True):
        st.subheader("📄 Hisobotni saqlash")
        
        child_status = "Ha" if with_child else "Yo'q"

        report_text = f"""
==================================================
FUQAROLIK HUJJATLARI TEKSHIRUV MANTIG'I (38-MODDA)
Sana: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
--------------------------------------------------
Tanlangan tartib: {procedure}
Yosh bola kiritilganmi: {child_status}

[TAYYOR HUJJATLAR ({len(completed_docs)}/{total})]:
""" + "\n".join([f"- {doc}" for doc in completed_docs]) + f"""

[YETISHMAYOTGAN HUJJATLAR ({len(missing_docs)}/{total})]:
""" + "\n".join([f"- {doc}" for doc in missing_docs]) + """
==================================================
"""

        st.download_button(
            label="📥 Hisobotni yuklab olish (.txt)",
            data=report_text,
            file_name=f"fuqarolik_hujjatlar_{datetime.date.today()}.txt",
            mime="text/plain",
            use_container_width=True
        )
