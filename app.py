import streamlit as st
import datetime

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Portali | 38-modda",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. "Huquqiy Tarmoq" - AI Neyrotarmog'i (Streamlit Cloud uchun 100% CSS)
st.markdown("""
    <style>
    /* 1. Asosiy Fon: Tungi osmon, to'q binafsha va ko'k */
    .stApp {
        background-color: #07051a !important;
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(124, 58, 237, 0.15), transparent 50%),
            radial-gradient(circle at 85% 30%, rgba(236, 72, 153, 0.15), transparent 50%);
        overflow-x: hidden;
        background-attachment: fixed;
    }

    /* 2. Tarmoq naqshi (Grid / Network) cheksiz harakati */
    .network-overlay {
        position: fixed;
        top: 0; left: 0;
        width: 200vw; height: 200vh;
        /* Sof CSS yordamida chizilgan tarmoq chiziqlari va nuqtalar */
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='150' viewBox='0 0 150 150'%3E%3Cpath d='M0,0 L150,150 M150,0 L0,150' stroke='rgba(139, 92, 246, 0.08)' stroke-width='1.5'/%3E%3Ccircle cx='75' cy='75' r='2.5' fill='rgba(236, 72, 153, 0.3)'/%3E%3C/svg%3E");
        background-size: 150px 150px;
        animation: moveGrid 40s linear infinite;
        z-index: 0;
        pointer-events: none;
        opacity: 0.9;
    }

    @keyframes moveGrid {
        0% { transform: translate(0, 0); }
        100% { transform: translate(-150px, -150px); }
    }

    /* 3. Suzuvchi Neyron Nuqtalar (Data Nodes) */
    .node {
        position: fixed;
        border-radius: 50%;
        background: #ec4899;
        box-shadow: 0 0 15px 4px rgba(236, 72, 153, 0.6);
        z-index: 1;
        pointer-events: none;
        opacity: 0.7;
    }

    /* Har bir tugun uchun o'lcham, joylashuv va parvoz yo'nalishi */
    .n1 { width: 6px; height: 6px; top: 10%; left: -10%; animation: fly1 18s linear infinite; }
    .n2 { width: 9px; height: 9px; top: 70%; right: -10%; background: #8b5cf6; box-shadow: 0 0 18px 5px rgba(139, 92, 246, 0.6); animation: fly2 22s linear infinite; }
    .n3 { width: 5px; height: 5px; top: -10%; left: 40%; animation: fly3 15s linear infinite; }
    .n4 { width: 8px; height: 8px; bottom: -10%; left: 30%; background: #06b6d4; box-shadow: 0 0 15px 4px rgba(6, 182, 212, 0.6); animation: fly4 25s linear infinite; }
    .n5 { width: 7px; height: 7px; top: 80%; left: -10%; animation: fly1 20s linear infinite; animation-delay: 5s; }
    .n6 { width: 10px; height: 10px; top: 20%; right: -10%; background: #8b5cf6; box-shadow: 0 0 15px 4px rgba(139, 92, 246, 0.6); animation: fly2 19s linear infinite; animation-delay: 7s; }
    .n7 { width: 6px; height: 6px; bottom: -10%; right: 40%; background: #ec4899; animation: fly3 21s linear infinite; animation-delay: 3s; }
    
    @keyframes fly1 { 0% { transform: translate(0, 0); } 100% { transform: translate(120vw, 30vh); } }
    @keyframes fly2 { 0% { transform: translate(0, 0); } 100% { transform: translate(-120vw, -40vh); } }
    @keyframes fly3 { 0% { transform: translate(0, 0); } 100% { transform: translate(40vw, 120vh); } }
    @keyframes fly4 { 0% { transform: translate(0, 0); } 100% { transform: translate(-60vw, -120vh); } }

    /* --- HI-TECH SHISHA (GLASSMORPHISM) INTERFEYS --- */
    
    /* Yon panel (Sidebar) */
    [data-testid="stSidebar"] {
        background: rgba(7, 5, 26, 0.65) !important;
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border-right: 1px solid rgba(139, 92, 246, 0.25);
    }

    /* Asosiy bloklar */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(12, 8, 30, 0.55) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 18px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 0 15px rgba(236, 72, 153, 0.08) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        position: relative;
        z-index: 10;
    }

    /* Blok ustiga sichqoncha borganda (Neon chaqnash) */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(236, 72, 153, 0.8) !important;
        box-shadow: 0 0 25px rgba(236, 72, 153, 0.4), inset 0 0 20px rgba(236, 72, 153, 0.15) !important;
        transform: translateY(-4px);
    }

    /* Matnlar */
    h1, h2, h3, h4 { 
        color: #fdf2f8 !important; 
        text-shadow: 0 2px 10px rgba(236, 72, 153, 0.5); 
        letter-spacing: 0.5px;
    }
    label, p, span, .stMarkdown { color: #cbd5e1 !important; }

    /* Tugmalar dizayni */
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(135deg, #7c3aed 0%, #db2777 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(219, 39, 119, 0.4) !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        box-shadow: 0 6px 25px rgba(124, 58, 237, 0.7) !important;
        transform: translateY(-2px) scale(1.02);
    }
    </style>
    
    <!-- Tarmoq chiziqlari va Suzuvchi Neyronlar -->
    <div class="network-overlay"></div>
    <div class="node n1"></div>
    <div class="node n2"></div>
    <div class="node n3"></div>
    <div class="node n4"></div>
    <div class="node n5"></div>
    <div class="node n6"></div>
    <div class="node n7"></div>
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
