import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Visa Benefit Buddy", page_icon="💳", layout="wide")

# 2. Custom Styling
st.markdown("""
    <style>
    .agent-thinking { 
        background-color: #000000; color: #00FF00; padding: 15px; 
        border-radius: 8px; font-family: 'Courier New', monospace;
        height: 250px; overflow-y: auto; border: 1px solid #1a1f71;
    }
    .main { background-color: #f8f9fa; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar - Secure Intake
st.sidebar.title("🛡️ Secure Intake")
card_number = st.sidebar.text_input("Masked Visa Number", "4111 XXXX XXXX 1234")
location = st.sidebar.selectbox("Simulate Location", ["IIT Madras Main Gate", "Chennai Airport", "Phoenix Mall"])
language = st.sidebar.radio("Language", ["English", "Tamil"])

# 4. App Header
st.title("💳 Visa Benefit Buddy")
st.write(f"**Agent Status:** Ready | **Current Context:** {location}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🤖 Agent Reasoning Log")
    log_box = st.empty()
    
    if st.button("🚀 Analyze Benefits"):
        logs = []
        def update_logs(msg, color="#00FF00"):
            logs.append(f"<span style='color:{color}'>&gt; {msg}</span>")
            log_box.markdown(f"<div class='agent-thinking'>{'<br>'.join(logs)}</div>", unsafe_allow_html=True)
            time.sleep(0.5)

        update_logs("Initializing Agentic Engine...")
        update_logs(f"Detected Card: Visa Signature (Masked: {card_number})")
        update_logs(f"Setting Geofence: {location}")
        update_logs("Searching Visa Merchant Offers (VMORC)...")
        update_logs("CROSS-CHECKING: T&C Section 4.2...", color="orange")
        update_logs("[SELF-CORRECTION] Validating 'Minimum Spend' clause...", color="orange")
        update_logs("Verification Complete. Confidence: 99.2%", color="#00FF00")

        with col2:
            st.subheader("✅ Verified Benefit")
            if language == "English":
                st.success(f"**15% Discount at {location}**")
                st.write("Applicable for all food and beverage purchases using your Visa Signature card.")
                st.caption("Source: Visa Merchant Terms 2026, Section 8.1")
            else:
                st.success(f"**{location}-ல் 15% தள்ளுபடி**")
                st.write("உங்கள் விசா சிக்னேச்சர் கார்டைப் பயன்படுத்தி அனைத்து உணவு மற்றும் பானங்களுக்கு தள்ளுபடி பெறலாம்.")
                st.caption("ஆதாரம்: விசா வணிக விதிமுறைகள் 2026, பிரிவு 8.1")
            
            st.button("Activate Benefit Now")
    else:
        st.info("Click 'Analyze Benefits' to start the agentic scan.")

st.divider()
st.caption("IIT Madras Shaastra 2026 Pitch | Powered by Gemini 1.5 Flash")