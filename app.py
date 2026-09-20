import streamlit as st
import datetime

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Portali | 38-modda",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)
import streamlit as st

st.markdown("""
    <style>
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e3a8a, #1e293b, #0f172a);
        background-size: 400% 400%;
        animation: gradientAnimation 12s ease infinite;
    }
    </style>
""", unsafe_allow_html=True)
# 2. Yon panel (Sidebar)
with st.sidebar:
    st.title("⚖️ LexiDraft Portal")
    st.info(
        "**38-modda toʻgʻrisida:**\n\n"
        "Oʻzbekiston Respublikasining Fuqarolik toʻgʻrisidagi Qonuniga muvofiq, "
        "iltimosnomalarga ilova qilinishi shart boʻlgan rasmiy hujjatlar roʻyxati."
    )
    st.divider()
    st.caption("Avtomatlashtirilgan huquqiy tahlil tizimi")

# 3. Asosiy sarlavha
st.title("⚖️ Fuqarolik Iltimosnomasi Hujjatlar Portali")
st.caption("Oʻzbekiston Respublikasi Fuqarolik toʻgʻrisidagi Qonunining 38-moddasi asosida avtomatlashtirilgan tekshirish")
st.divider()

# 4. Ikki ustunli struktura
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
