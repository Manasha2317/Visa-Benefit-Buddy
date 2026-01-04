# Visa Benefit Buddy (VBB) 💳
**An Agentic Concierge for Proactive Credit Card Benefit Utilization**

### 🚀 Overview
VBB is a proactive AI agent designed to bridge the gap between complex credit card T&Cs and real-time consumer intent. Built for the **Shaastra 2026** hackathon.

### 🛠️ Key Technical Features
- **Self-Correction Loop:** Uses a dual-agent architecture to verify AI-generated summaries against raw T&C text to eliminate hallucinations.
- **Privacy-First:** Implements local regex masking to ensure PII (Full Card Numbers) never leave the local environment.
- **Bilingual Support:** Full English and Tamil support for local inclusivity in Chennai.

### 💻 Tech Stack
- **Orchestration:** LangGraph (Agentic Workflow)
- **Intelligence:** Gemini 1.5 Flash
- **Frontend:** Streamlit
- **Data:** Visa VMORC & VCES API (Sandbox Mocks)

### 🏃 Setup
1. `pip install -r requirements.txt`
2. `streamlit run app.py`
