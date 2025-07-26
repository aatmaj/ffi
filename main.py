import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(layout="wide", page_title="Field Force Intelligence vs Traditional Workflow")

# Custom CSS for better UI
st.markdown("""
    <style>
        .main {
            background-color: #f9fafc;
        }
        .block-container {
            padding-top: 2rem;
        }
        h1, h2, h3 {
            color: #1f4e79;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            border-radius: 10px;
        }
        .stButton>button {
            border-radius: 10px;
            background-color: #0052cc;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🧠 Field Force Intelligence – System of Work vs Traditional CRM Workflow")

st.markdown("""
### 💡 Goal:
Create a self-explanatory, interactive product demo showing how **Field Force Intelligence** (built on MCP) outperforms traditional workflows.
""")

# Layout: Two side-by-side panels
col1, col2 = st.columns(2, gap="large")

# --- Left Panel: Traditional CRM Workflow --- #
with col1:
    st.header("🗂️ Traditional CRM Workflow")
    st.markdown("---")

    with st.container():
        with st.expander("1️⃣ Filters and Target List"):
            st.text("CRM Dashboard > Region: Bangalore South")
            st.text("Speciality: Cardiologist")
            st.text("Click 'Download Target List' → Opens Excel")
            st.warning("Manual workflows. Static logic. No context-awareness.")

        with st.expander("2️⃣ Manual Review"):
            st.text("Check last visit dates manually in Excel")
            st.text("Open sales deck folder")
            st.text("Send bulk WhatsApp/email")

        with st.expander("3️⃣ Summary"):
            st.markdown("""
            - Manual filters and downloads
            - Static PDF decks
            - Generic messaging
            """)

# --- Right Panel: Field Force Intelligence (MCP) --- #
with col2:
    st.header("🤖 Field Force Intelligence – System of Work (MCP)")
    st.markdown("---")

    with st.container():
        with st.expander("1️⃣ Ask a Natural Language Question"):
            query = st.text_input("🗨️ You:", "Who should I meet in Bangalore South today?")
            if query:
                st.success("Top 3 priorities:")
                st.markdown("""
                1. **Dr. Mehta** — Rising Telmisartan usage, not met in 12 days  
                2. **Dr. Ramesh** — Competitor Rx spiking  
                3. **Dr. Anitha** — Responded positively last time  
                🧭 Route built with optimal timing
                """)

        with st.expander("2️⃣ View Optimized Plan"):
            st.map({
                "lat": [12.92, 12.94, 12.96],
                "lon": [77.61, 77.63, 77.65]
            })
            st.markdown("Each doctor has a custom narrative built from win history.")

        with st.expander("3️⃣ Personalized Pitch Generation"):
            pitch_request = st.text_input("🗨️ You:", "Suggest pitch for Dr. Mehta")
            if pitch_request:
                st.info("Dr. Mehta previously objected on price. Use comparison narrative with brand X showing 15% adherence improvement. Want me to log this after the call?")
                if st.button("✅ Use & Schedule"):
                    st.success("Call scheduled and pitch saved.")

        with st.expander("4️⃣ Day-End Impact Summary"):
            if st.button("📈 Show Daily Summary"):
                st.success("""
                - Visited 5 doctors  
                - Logged 2 engagements  
                - Dr. Mehta showed conversion interest  
                - Est. uplift: ₹1.8L/month  
                - Insights added to next week’s plan
                """)

# Final Comparison
st.markdown("---")
st.subheader("🎯 Final Comparison")
col1_final, col2_final = st.columns(2, gap="large")

with col1_final:
    st.markdown("""
    **📉 Traditional CRM Workflow**
    - Manual filtering + Excel + generic decks
    - Static target lists
    - Reactive logging
    """)

with col2_final:
    st.markdown("""
    **🚀 Field Force Intelligence (MCP System of Work)**
    - Context-aware plans + custom narratives
    - Dynamic, personalized doctor suggestions
    - Proactive outcome tracking & learning
    """)

st.markdown("""
> 🧠 You didn’t run reports. You didn’t search files.  
> You just worked — and the system *worked with you*.  
> 
> *This is not workflow automation. This is a System of Work.*  
> *Built with MCP.*
""")