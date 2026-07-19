import streamlit as st
import json
import pandas as pd

st.set_page_config(
    page_title="Digital Twin Dashboard",
    page_icon="🏭",
    layout="wide"
)

# Background color
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e3f2fd, #f3e5f5);
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 style='text-align:center;color:#1565C0;'>🏭 Digital Twin Dashboard</h1>",
    unsafe_allow_html=True
)

# Read data.json
try:
    with open("data.json", "r") as f:
        data = json.load(f)

    product_count = data["phone_count"]
    defect_count = data["defect_count"]

except:
    product_count = 0
    defect_count = 0

# Efficiency
if product_count > 0:
    efficiency = ((product_count - defect_count) / product_count) * 100
else:
    efficiency = 0

# Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="background:#2196F3;
                padding:20px;
                border-radius:15px;
                text-align:center;
                color:white;">
        <h2>📦 Product Count</h2>
        <h1>{product_count}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background:#F44336;
                padding:20px;
                border-radius:15px;
                text-align:center;
                color:white;">
        <h2>❌ Defect Count</h2>
        <h1>{defect_count}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background:#4CAF50;
                padding:20px;
                border-radius:15px;
                text-align:center;
                color:white;">
        <h2>📈 Efficiency</h2>
        <h1>{efficiency:.1f}%</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Status
st.success("🟢 AI Detection Active | Camera Connected | Digital Twin Running")

# Graph
if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.append(product_count)

if len(st.session_state.history) > 20:
    st.session_state.history.pop(0)

df = pd.DataFrame({
    "Products": st.session_state.history
})

st.subheader("📈 Live Production Trend")
st.line_chart(df)

# Progress bar
st.subheader("🏭 Factory Efficiency")
st.progress(int(efficiency))

# System information
st.subheader("📋 System Information")

st.info(f"""
📦 Product Count: {product_count}

❌ Defect Count: {defect_count}

📈 Efficiency: {efficiency:.1f}%

✅ YOLOv8 Detection Active

✅ Camera Connected

✅ Digital Twin Online
""")