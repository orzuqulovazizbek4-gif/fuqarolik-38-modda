import streamlit as st
import datetime

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Portali | 38-modda",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SOF CSS3 Pasportlar Animatsiyasi va Premium Tilla-Shisha (Gold-Glass) Dizayn
st.markdown("""
    <style>
    /* 1. Asosiy Fon Gradienti - Chuqur va Rasmiy */
    .stApp {
        background: linear-gradient(-45deg, #050a15, #0f172a, #061122, #020617);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. Passport Animatsiyasi Konteyneri (Orqa fon) */
    .passport-area {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        overflow: hidden;
        z-index: 0; 
        pointer-events: none; /* Sichqoncha halaqit bermasligi uchun */
    }

    /* 3. Pasportlarning Mukammal 3D Dizayni */
    .pass-item {
        position: absolute;
        width: 65px; height: 95px;
        background: linear-gradient(135deg, #0a3622, #115c3a); /* O'zbekiston pasporti yashil rangi */
        border-radius: 6px;
        border: 1px solid #d4af37; /* Tilla rang hoshiya */
        box-shadow: 4px 8px 20px rgba(0,0,0,0.6), inset 0 0 10px rgba(212, 175, 55, 0.3);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        opacity: 0;
    }
    .pass-item::before {
        content: '🇺🇿'; /* Pasport belgisi */
        font-size: 28px;
        margin-bottom: 5px;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));
    }
    .pass-item::after {
        content: 'PASPORT';
        font-size: 8px;
        color: #d4af37;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
        letter-spacing: 1px;
        text-shadow: 0 1px 2px rgba(0,0,0,0.8);
    }

    /* 4. Pasportlarning turli uchish traektoriyalari */
    @keyframes flyUp1 {
        0% { transform: translateY(110vh) translateX(0px) rotate(-25deg) scale(0.8); opacity: 0; }
        10% { opacity: 0.65; } 90% { opacity: 0.65; }
        100% { transform: translateY(-20vh) translateX(200px) rotate(45deg) scale(1.2); opacity: 0; }
    }
    @keyframes flyUp2 {
        0% { transform: translateY(110vh) translateX(0px) rotate(35deg) scale(1.1); opacity: 0; }
        10% { opacity: 0.5; } 90% { opacity: 0.5; }
        100% { transform: translateY(-20vh) translateX(-150px) rotate(-30deg) scale(0.7); opacity: 0; }
    }
    @keyframes flyUp3 {
        0% { transform: translateY(110vh) translateX(0px) rotate(0deg) scale(0.9); opacity: 0; }
        10% { opacity: 0.7; } 90% { opacity: 0.7; }
        100% { transform: translateY(-20vh) translateX(80px) rotate(90deg) scale(1); opacity: 0; }
    }

    /* 5. Har bir pasport uchun alohida joylashuv, tezlik va vaqt */
    .p1 { left: 10%; animation: flyUp1 14s linear infinite; }
    .p2 { left: 25%; animation: flyUp2 17s linear infinite; animation-delay: 2s; }
    .p3 { left: 40%; animation: flyUp3 20s linear infinite; animation-delay: 5s; }
    .p4 { left: 60%; animation: flyUp1 15s linear infinite; animation-delay: 1s; }
    .p5 { left: 75%; animation: flyUp2 18s linear infinite; animation-delay: 7s; }
    .p6 { left: 90%; animation: flyUp3 14s linear infinite; animation-delay: 3s; }
    .p7 { left: 5%;  animation: flyUp2 22s linear infinite; animation-delay: 9s; }
    .p8 { left: 50%; animation: flyUp1 16s linear infinite; animation-delay: 11s; }
    .p9 { left: 85%; animation: flyUp3 19s linear infinite; animation-delay: 13s; }
    .p10 { left: 35%; animation: flyUp2 15s linear infinite; animation-delay: 16s; }
    .p11 { left: 15%; animation: flyUp1 21s linear infinite; animation-delay: 8s; }
    .p12 { left: 65%; animation: flyUp3 17s linear infinite; animation-delay: 4s; }

    /* --- UI KONTEYNERLAR UCHUN PREMIUM DIZAYN --- */
    [data-testid="stSidebar"] {
        background: rgba(4, 9, 20, 0.8) !important;
        backdrop-filter: blur(25px);
        border-right: 1px solid rgba(212, 175, 55, 0.25); /* Tilla rang hoshiya */
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(10, 18, 35, 0.65) !important;
        backdrop-filter: blur(20px) saturate(200%) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(212, 175, 55, 0.35) !important;
        border-radius: 20px !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7), inset 0 0 20px rgba(212, 175, 55, 0.1) !important;
        transition: all 0.4s ease !important;
        z-index: 10;
        position: relative;
    }

    /* Sichqoncha olib kelinganda blok tilla rangda chaqnaydi */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(212, 175, 55, 0.9) !important;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.3), inset 0 0 25px rgba(212, 175, 55, 0.2) !important;
        transform: translateY(-5px);
    }

    /* Sarlavhalarga tilla rang (Gold) berish */
    h1, h2, h3, h4 { color: #d4af37 !important; text-shadow: 0 3px 6px rgba(0,0,0,0.8); }
    label, span, p { color: #e2e8f0 !important; }

    /* Tugmalar Dizayni - Yashil va Tilla rang uyg'unligi */
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(135deg, #0a3622 0%, #115c3a 100%) !important;
        color: #d4af37 !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: 1px solid #d4af37 !important;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.6) !important;
        transform: translateY(-2px) scale(1.02);
        color: #fff !important;
    }
    </style>

    <!-- HTML Elementlar (Animatsiya qilinadigan 12 ta pasport) -->
    <div class="passport-area">
        <div class="pass-item p1"></div>
        <div class="pass-item p2"></div>
        <div class="pass-item p3"></div>
        <div class="pass-item p4"></div>
        <div class="pass-item p5"></div>
        <div class="pass-item p6"></div>
        <div class="pass-item p7"></div>
        <div class="pass-item p8"></div>
        <div class="pass-item p9"></div>
        <div class="pass-item p10"></div>
        <div class="pass-item p11"></div>
        <div class="pass-item p12"></div>
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
