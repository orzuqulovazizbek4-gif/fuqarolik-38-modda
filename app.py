import streamlit as st
import datetime

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Fuqarolik Hujjatlari Portali | 38-modda",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Interaktiv 3D HTML5 Canvas Zarralar va Obyektlar Harakati
st.markdown("""
    <canvas id="bgCanvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; pointer-events: none;"></canvas>
    
    <script>
    const canvas = document.getElementById('bgCanvas');
    const ctx = canvas.getContext('2d');

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    const particles = [];
    const numParticles = 65;
    const symbols = ['⚖️', '📜', '🛡️', '🏛️'];

    for (let i = 0; i < numParticles; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 1.6,
            vy: (Math.random() - 0.5) * 1.6,
            radius: Math.random() * 3 + 1.5,
            symbol: Math.random() < 0.2 ? symbols[Math.floor(Math.random() * symbols.length)] : null,
            size: Math.random() * 22 + 16,
            color: `hsl(${Math.random() * 80 + 220}, 90%, 65%)`,
            pulse: Math.random() * Math.PI
        });
    }

    let mouse = { x: null, y: null };
    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        let gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
        gradient.addColorStop(0, '#060814');
        gradient.addColorStop(0.5, '#0d1329');
        gradient.addColorStop(1, '#050611');
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for (let i = 0; i < particles.length; i++) {
            let p = particles[i];

            p.x += p.vx;
            p.y += p.vy;

            if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
            if (p.y < 0 || p.y > canvas.height) p.vy *= -1;

            p.pulse += 0.03;

            if (p.symbol) {
                ctx.font = `${p.size}px Arial`;
                ctx.globalAlpha = 0.75 + Math.sin(p.pulse) * 0.25;
                ctx.fillText(p.symbol, p.x, p.y);
                ctx.globalAlpha = 1.0;
            } else {
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius + Math.sin(p.pulse) * 1.5, 0, Math.PI * 2);
                ctx.fillStyle = p.color;
                ctx.shadowBlur = 15;
                ctx.shadowColor = p.color;
                ctx.fill();
                ctx.shadowBlur = 0;
            }

            for (let j = i + 1; j < particles.length; j++) {
                let p2 = particles[j];
                let dx = p.x - p2.x;
                let dy = p.y - p2.y;
                let dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 140) {
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.strokeStyle = `rgba(139, 92, 246, ${1 - dist / 140})`;
                    ctx.lineWidth = 0.9;
                    ctx.stroke();
                }
            }

            if (mouse.x && mouse.y) {
                let mdx = p.x - mouse.x;
                let mdy = p.y - mouse.y;
                let mdist = Math.sqrt(mdx * mdx + mdy * mdy);
                if (mdist < 190) {
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.strokeStyle = `rgba(236, 72, 153, ${1 - mdist / 190})`;
                    ctx.lineWidth = 1.4;
                    ctx.stroke();
                }
            }
        }

        requestAnimationFrame(animate);
    }
    animate();
    </script>

    <style>
    /* Streamlit interfeysini shaffoflashtirish va uslub berish */
    .stApp {
        background: transparent !important;
    }

    [data-testid="stSidebar"] {
        background: rgba(8, 12, 28, 0.75) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(13, 19, 41, 0.65) !important;
        backdrop-filter: blur(18px) !important;
        -webkit-backdrop-filter: blur(18px) !important;
        border: 1px solid rgba(139, 92, 246, 0.35) !important;
        border-radius: 22px !important;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6) !important;
        transition: all 0.4s ease-in-out !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(236, 72, 153, 0.85) !important;
        box-shadow: 0 0 35px rgba(236, 72, 153, 0.5) !important;
        transform: translateY(-5px);
    }

    h1, h2, h3, h4, label, span, p {
        color: #FFFFFF !important;
        text-shadow: 0 2px 5px rgba(0,0,0,0.7);
    }

    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(135deg, #7C3AED 0%, #DB2777 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0 5px 20px rgba(219, 39, 119, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        box-shadow: 0 8px 30px rgba(124, 58, 237, 0.85) !important;
        transform: scale(1.03);
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
