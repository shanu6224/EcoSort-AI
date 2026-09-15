
import streamlit as st
from PIL import Image

st.set_page_config(page_title="EcoSort AI", page_icon="♻️", layout="wide")

WASTE = {
    "Plastic Bottle": {
        "category": "Recyclable",
        "confidence": 96,
        "bin": "Recyclable / Plastic",
        "reason": "The item has the visual characteristics of a common PET plastic bottle.",
        "action": "Empty the bottle and place it in the designated recyclable/plastic collection.",
        "tip": "Choose a reusable bottle when possible to reduce single-use plastic."
    },
    "Banana Peel": {
        "category": "Organic",
        "confidence": 98,
        "bin": "Organic / Compost",
        "reason": "The item appears to be biodegradable food waste.",
        "action": "Place it in the organic or compost collection.",
        "tip": "Composting food waste can return nutrients to soil."
    },
    "Paper": {
        "category": "Recyclable",
        "confidence": 94,
        "bin": "Paper / Recyclable",
        "reason": "The item appears to be clean paper suitable for recycling.",
        "action": "Keep it dry and place it in the paper/recyclable collection.",
        "tip": "Reduce unnecessary printing and reuse paper where possible."
    },
    "Battery": {
        "category": "E-Waste",
        "confidence": 99,
        "bin": "Authorized E-Waste Collection",
        "reason": "The item appears to be a portable battery.",
        "action": "Do not place it in general waste. Hand it to an authorized battery/e-waste collection point.",
        "tip": "Keeping batteries separate helps prevent unsafe disposal and contamination."
    },
    "Food Container": {
        "category": "General / Check Local Rule",
        "confidence": 82,
        "bin": "Check Campus Waste Policy",
        "reason": "Food containers can be recyclable or general waste depending on material and contamination.",
        "action": "Empty and clean it if possible, then follow the campus/local waste policy.",
        "tip": "Reusable food containers can reduce disposable packaging."
    }
}

if "selected" not in st.session_state:
    st.session_state.selected = None
if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("""
<style>
.block-container {padding-top: 2rem; padding-bottom: 2rem; max-width: 1200px;}
.hero {padding: 22px 26px; border-radius: 18px; background: linear-gradient(135deg,#e9f7ef,#f6fbf8); border:1px solid #d7eadf;}
.badge {display:inline-block; padding:5px 11px; border-radius:20px; background:#dff3e7; font-size:13px; font-weight:600;}
.card {padding:18px; border-radius:15px; border:1px solid #e5e7eb; background:#fff; margin:8px 0;}
.small {color:#64748b; font-size:14px;}
.result {padding:22px; border-radius:18px; border:1px solid #d9e8df; background:#fbfffc;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<span class="badge">SDG 12 • Responsible Consumption & Production</span>
<h1>♻️ EcoSort AI</h1>
<h3>AI-Powered Waste Segregation & Sustainable Disposal Assistant</h3>
<p>Identify • Segregate • Sustain</p>
</div>
""", unsafe_allow_html=True)

st.write("")

left, right = st.columns([1, 1.35], gap="large")

with left:
    st.subheader("📷 Scan Waste")
    uploaded = st.file_uploader("Upload a waste image", type=["jpg","jpeg","png"])

    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded waste image", use_container_width=True)

    st.markdown("**Demo mode**")
    st.caption("Select a sample recognition result to demonstrate the complete AI workflow.")
    choice = st.selectbox("Sample object", list(WASTE.keys()))

    if st.button("🤖 Analyze with EcoSort AI", type="primary", use_container_width=True):
        st.session_state.selected = choice
        st.session_state.history.insert(0, choice)

with right:
    st.subheader("🔎 AI Analysis")

    if st.session_state.selected:
        item = st.session_state.selected
        data = WASTE[item]

        st.markdown('<div class="result">', unsafe_allow_html=True)
        a, b = st.columns(2)
        a.metric("Detected Item", item)
        b.metric("AI Confidence", f'{data["confidence"]}%')

        st.write(f"**Category:** {data['category']}")
        st.write(f"**Recommended Collection:** {data['bin']}")
        st.write(f"**Why:** {data['reason']}")

        st.markdown("### ♻️ Recommended Action")
        st.info(data["action"])

        st.markdown("### 🌱 Sustainability Tip")
        st.success(data["tip"])

        if data["category"] in ["E-Waste", "Hazardous/Special"]:
            st.warning("⚠️ Special-handling item: follow authorized/local disposal guidance.")

        st.caption("Prototype note: classification results shown here are simulated demo outputs for presentation.")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Upload an image and click **Analyze with EcoSort AI** to see the result.")

st.divider()

st.subheader("⚙️ How EcoSort AI Works")
c1, c2, c3, c4 = st.columns(4)
c1.markdown("### 1️⃣ Input\nWaste image")
c2.markdown("### 2️⃣ AI\nImage understanding")
c3.markdown("### 3️⃣ Decision\nCategory + disposal guidance")
c4.markdown("### 4️⃣ Impact\nSustainable action")

st.divider()

st.subheader("📊 Demo Activity")
if st.session_state.history:
    counts = {}
    for x in st.session_state.history:
        counts[x] = counts.get(x, 0) + 1
    cols = st.columns(min(4, len(counts)))
    for i, (k,v) in enumerate(counts.items()):
        cols[i % len(cols)].metric(k, v)
else:
    st.caption("No demo scans yet.")

st.divider()

st.subheader("🛡️ Responsible AI")
r1, r2, r3, r4 = st.columns(4)
r1.markdown("**Transparency**\nShows reason and confidence.")
r2.markdown("**Uncertainty**\nAvoids forced certainty for ambiguous items.")
r3.markdown("**Privacy**\nAvoid unnecessary personal information in images.")
r4.markdown("**Safety**\nSpecial waste is routed to authorized guidance.")

st.caption("EcoSort AI is a decision-support prototype, not a replacement for local waste-management rules or trained personnel.")
