import streamlit as st
import datetime

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Portali | 38-modda",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Murakkab va rang-barang CSS animatsiyasi + Shaffof shisha (Glassmorphism) dizayni
st.markdown("""
    <style>
    /* Aurora Mesh rang-barang harakatlanuvchi fon animatsiyasi */
    @keyframes auroraMesh {
        0% {
            background-position: 0% 0%, 100% 100%, 0% 100%, 100% 0%;
            filter: hue-rotate(0deg);
        }
        50% {
            background-position: 100% 100%, 0% 0%, 100% 0%, 0% 100%;
            filter: hue-rotate(180deg);
        }
        100% {
            background-position: 0% 0%, 100% 100%, 0% 100%, 100% 0%;
            filter: hue-rotate(360deg);
        }
    }

    .stApp {
        background: 
            radial-gradient(circle at 10% 20%, rgba(124, 58, 237, 0.6) 0%, transparent 40%),
            radial-gradient(circle at 90% 20%, rgba(6, 182, 212, 0.6) 0%, transparent 40%),
            radial-gradient(circle at 50% 80%, rgba(236, 72, 153, 0.6) 0%, transparent 40%),
            radial-gradient(circle at 80% 80%, rgba(59, 130, 246, 0.6) 0%, transparent 40%),
            linear-gradient(135deg, #090D16 0%, #05050F 100%);
        background-size: 200% 200%;
        animation: auroraMesh 15s ease-in-out infinite alternate;
        background-attachment: fixed;
    }

    /* Yon panelni shaffoflashtirish */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(16px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Konteynerlarga Shaffof Shisha va Neon Nur effekti */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        border-radius: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
        transition: all 0.4s ease-in-out !important;
    }

    /* Sichqoncha olib kelinganda yonish effekti */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(168, 85, 247, 0.8) !important;
        box-shadow: 0 0 25px rgba(168, 85, 247, 0.5) !important;
        transform: translateY(-3px);
    }

    /* Sarlavha va matnlar ko'rinishini yaxshilash */
    h1, h2, h3, h4, label, span, p {
        color: #FFFFFF !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }

    /* Tugmalarga neon dizayn */
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        box-shadow: 0 6px 25px rgba(139, 92, 246, 0.8) !important;
        transform: scale(1.02);
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
