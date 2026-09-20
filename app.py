import streamlit as st
import datetime

# Sahifa sozlamalari
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Tekshiruvi (38-modda)",
    page_icon="⚖️",
    layout="centered"
)

# Tashqi ko'rinish uchun CSS uslublari
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #008080;
    }
    .report-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #008080;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚖️ Fuqarolik Iltimosnomasi Hujjatlar Tekshiruvi")
st.caption("Oʻzbekiston Respublikasining Fuqarolik toʻgʻrisidagi Qonunining 38-moddasi asosida ishlab chiqilgan")

st.write("---")

# 1. Tartibni tanlash
procedure = st.selectbox(
    "**Topshirilayotgan iltimosnoma turini tanlang:**",
    [
        "Umumiy tartibda qabul qilish yoki fuqarolikni tiklash",
        "Soddalashtirilgan tartibda qabul qilish",
        "Alohida tartibda qabul qilish"
    ]
)

# Dynamic variantlar
with_child = False
if procedure != "Alohida tartibda qabul qilish":
    with_child = st.checkbox("Iltimosnomada yosh bola (farzand) ko'rsatilganmi?")

# 2. 38-modda mantiqiga ko'ra hujjatlar ro'yxatini shakllantirish
docs_required = []

if procedure == "Alohida tartibda qabul qilish":
    docs_required = [
        "Pasport yoki identifikatsiyalovchi karta (yashash guvohnomasi)"
    ]
else:
    # Umumiy, Tiklash va Soddalashtirilgan tartib uchun tayanch hujjatlar
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

st.subheader("📋 Talab etiladigan hujjatlar nazorat roʻyxati")

# Interactive checklist
completed_docs = []
missing_docs = []

for idx, doc in enumerate(docs_required, 1):
    status = st.checkbox(f"{idx}. {doc}", key=f"doc_{idx}")
    if status:
        completed_docs.append(doc)
    else:
        missing_docs.append(doc)

# 3. Progress va Analiz
total = len(docs_required)
current = len(completed_docs)
progress = current / total if total > 0 else 0

st.write("---")
st.subheader("📊 Tayyorgarlik darajasi")
st.progress(progress)
st.write(f"**Holat:** {total} ta hujjatdan **{current} ta**si tayyor ({int(progress * 100)}%).")

if current == total:
    st.success("✅ Barcha kerakli hujjatlar to'liq jamlandi! Iltimosnoma topshirishga tayyor.")
else:
    st.warning(f"⚠️ Yana {total - current} ta hujjat yetishmayapti.")

# 4. Eksport / Hujjat hisoboti
st.write("---")
st.subheader("📄 Natijani saqlash")

report_text = f"""
==================================================
FUQAROLIK HUJJATLARI TEKSHIRUV MANTIG'I (38-MODDA)
Sana: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
--------------------------------------------------
Tanlangan tartib: {procedure}
Yosh bola kiritilganmi: {'Ha' if with_child else 'Yo'q'}

[TAYYOR HUJJATLAR ({len(completed_docs)}/{total})]:
""" + "\n".join([f"- {doc}" for doc in completed_docs]) + f"""

[YETISHMAYOTGAN HUJJATLAR ({len(missing_docs)}/{total})]:
""" + "\n".join([f"- {doc}" for doc in missing_docs]) + """
==================================================
"""

st.download_button(
    label="📥 Tekshiruv hisobotini yuklab olish (.txt)",
    data=report_text,
    file_name=f"fuqarolik_hujjatlar_royxati_{datetime.date.today()}.txt",
    mime="text/plain"
)
