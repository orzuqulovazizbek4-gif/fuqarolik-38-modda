import streamlit as st
import datetime

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Portali | 38-modda",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 100% Ishlaydigan Sof CSS3 Murakkab Animatsiya va Shisha (Glassmorphism) Dizayn
st.markdown("""
    <style>
    /* Gradient va Rang-barang Suyuq Harakat Animatsiyasi */
    @keyframes liquidAurora {
        0% {
            background-position: 0% 50%;
            filter: hue-rotate(0deg) contrast(120%);
        }
        25% {
            background-position: 100% 0%;
            filter: hue-rotate(90deg) contrast(110%);
        }
        50% {
            background-position: 100% 100%;
            filter: hue-rotate(180deg) contrast(130%);
        }
        75% {
            background-position: 0% 100%;
            filter: hue-rotate(270deg) contrast(110%);
        }
        100% {
            background-position: 0% 50%;
            filter: hue-rotate(360deg) contrast(120%);
        }
    }

    /* Suzuvchi Nurli Halqalar Animatsiyasi */
    @keyframes floatingGlow {
        0% { transform: translate(0px, 0px) scale(1) rotate(0deg); }
        33% { transform: translate(30px, -50px) scale(1.1) rotate(120deg); }
        66% { transform: translate(-20px, 40px) scale(0.9) rotate(240deg); }
        100% { transform: translate(0px, 0px) scale(1) rotate(360deg); }
    }

    /* Asosiy Fon */
    .stApp {
        background: 
            radial-gradient(circle at 20% 20%, rgba(147, 51, 234, 0.7) 0%, transparent 40%),
            radial-gradient(circle at 80% 30%, rgba(236, 72, 153, 0.7) 0%, transparent 45%),
            radial-gradient(circle at 50% 80%, rgba(6, 182, 212, 0.7) 0%, transparent 40%),
            radial-gradient(circle at 80% 80%, rgba(59, 130, 246, 0.7) 0%, transparent 45%),
            linear-gradient(135deg, #070913 0%, #0c1023 50%, #05060d 100%);
        background-size: 200% 200%;
        animation: liquidAurora 12s ease-in-out infinite alternate;
        background-attachment: fixed;
    }

    /* Yon Panel (Sidebar) Uslubi */
    [data-testid="stSidebar"] {
        background: rgba(10, 15, 30, 0.75) !important;
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border-right: 1px solid rgba(255, 255, 255, 0.12);
    }

    /* Konteynerlar (Bloklar) - Ultra-Shisha va Neon Yoritish Effekti */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(15, 23, 42, 0.55) !important;
        backdrop-filter: blur(16px) saturate(190%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(190%) !important;
        border: 1px solid rgba(168, 85, 247, 0.4) !important;
        border-radius: 20px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(168, 85, 247, 0.15) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    /* Sichqoncha olib kelinganda bloklarning yonishi va ko'tarilishi */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(236, 72, 153, 0.9) !important;
        box-shadow: 0 0 30px rgba(236, 72, 153, 0.6), inset 0 0 20px rgba(236, 72, 153, 0.2) !important;
        transform: translateY(-6px) scale(1.01);
    }

    /* Matnlar va Sarlavhalar */
    h1, h2, h3, h4, label, span, p {
        color: #FFFFFF !important;
        text-shadow: 0 2px 6px rgba(0,0,0,0.6);
    }

    /* Tugmalar Dizayni */
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0 4px 20px rgba(236, 72, 153, 0.5) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        box-shadow: 0 6px 30px rgba(139, 92, 246, 0.9) !important;
        transform: translateY(-2px) scale(1.02);
    }
    </style>
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
st.title("⚖️ Fuqarolik Iltimosnomasi Hujjatlar Portali")
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
