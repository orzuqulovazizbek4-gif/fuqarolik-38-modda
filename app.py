import streamlit as st
import datetime

# 1. Sahifa sozlamalari (kengaytirilgan rejim va sarlavha)
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Portali | 38-modda",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Zamonaviy CSS dizayn uslublari
st.markdown("""
    <style>
    /* Asosiy fon */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Yuqori Banner (Hero Header) */
    .hero-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #0F172A 100%);
        padding: 30px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .hero-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #FFFFFF;
    }
    .hero-subtitle {
        font-size: 15px;
        color: #93C5FD;
        font-weight: 400;
    }

    /* Bloklar (Card) ko'rinishi */
    .custom-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        border: 1px solid #E2E8F0;
        margin-bottom: 20px;
    }

    /* Tayyorgarlik foiz ko'rsatkichi */
    .metric-box {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border-left: 5px solid #2563EB;
        padding: 18px;
        border-radius: 10px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* Tugmalar dizayni */
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3) !important;
        transform: translateY(-1px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Yon panel (Sidebar)
with st.sidebar:
    st.markdown("### ⚖️ LexiDraft Portal")
    st.info("""
    **38-modda toʻgʻrisida:**
    Oʻzbekiston Respublikasining Fuqarolik toʻgʻrisidagi Qonuniga muvofiq, iltimosnomalarga ilova qilinishi shart boʻlgan rasmiy hujjatlar roʻyxati.
    """)
    st.markdown("---")
    st.caption("Avtomatlashtirilgan huquqiy tahlil tizimi")

# 4. Yuqori sarlavha bansi
st.markdown("""
    <div class="hero-header">
        <div class="hero-title">⚖️ Fuqarolik Iltimosnomasi Hujjatlar Portali</div>
        <div class="hero-subtitle">Oʻzbekiston Respublikasi Fuqarolik toʻgʻrisidagi Qonunining 38-moddasi asosida avtomatlashtirilgan tekshirish</div>
    </div>
""", unsafe_allow_html=True)

# 5. Ikki ustunli zamonaviy struktura
col1, col2 = st.columns([1.2, 0.8], gap="large")

with col1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
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
    
    st.markdown('</div>', unsafe_allow_html=True)

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

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("📊 Tayyorgarlik holati")
    
    total = len(docs_required)
    current = len(completed_docs)
    progress = current / total if total > 0 else 0

    st.progress(progress)
    
    st.markdown(f"""
        <div class="metric-box">
            <h2 style="color: #1E3A8A; margin:0; font-size: 36px;">{int(progress * 100)}%</h2>
            <p style="margin:0; color: #475569; font-weight: 500;">{total} ta hujjatdan {current} tasi tayyor</p>
        </div>
    """, unsafe_allow_html=True)

    if current == total:
        st.success("🎉 Barcha kerakli hujjatlar to'liq jamlandi! Topshirishga tayyor.")
    else:
        st.warning(f"⚠️ Yana {total - current} ta hujjat yetishmayapti.")

    st.markdown('</div>', unsafe_allow_html=True)

    # Yuklab olish bloki
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)
