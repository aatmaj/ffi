import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
import time

# Page configuration
st.set_page_config(
    layout="wide", 
    page_title="Field Force Intelligence vs Traditional Workflow",
    page_icon="🧠",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS with better readability
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Inter', sans-serif;
        }
        
        .block-container {
            padding-top: 1rem;
            max-width: 1200px;
        }
        
        .hero-section {
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        .comparison-card {
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(15px);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
            border: 2px solid rgba(255, 255, 255, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .comparison-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.18);
        }
        
        .traditional-card {
            border-left: 6px solid #e74c3c;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(231, 76, 60, 0.05) 100%);
        }
        
        .ai-card {
            border-left: 6px solid #2ecc71;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(46, 204, 113, 0.05) 100%);
        }
        
        h1 {
            color: #1a252f !important;
            font-weight: 700 !important;
            text-align: center;
            margin-bottom: 0.5rem;
            font-size: 2.5rem !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        h2 {
            color: #2c3e50 !important;
            font-weight: 600 !important;
            margin-bottom: 1.5rem;
            font-size: 1.8rem !important;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }
        
        h3 {
            color: #1a252f !important;
            font-weight: 600 !important;
            font-size: 1.4rem !important;
            margin-bottom: 1rem;
        }
        
        h4 {
            color: #2c3e50 !important;
            font-weight: 500 !important;
            font-size: 1.1rem !important;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            margin: 0.5rem 0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .metric-card h2 {
            color: #fff !important;
            font-size: 2.2rem !important;
            margin: 0.5rem 0 !important;
            text-shadow: none !important;
        }
        
        .metric-card h3 {
            color: #ecf0f1 !important;
            font-size: 1.1rem !important;
            margin-bottom: 0.5rem !important;
            text-shadow: none !important;
        }
        
        .metric-card h4 {
            color: #ecf0f1 !important;
            font-size: 0.9rem !important;
            margin-bottom: 0.5rem !important;
            text-shadow: none !important;
        }
        
        .step-indicator {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: rgba(52, 73, 94, 0.05);
            border-radius: 10px;
            border-left: 4px solid #3498db;
        }
        
        .step-number {
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
            color: white;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            margin-right: 1.5rem;
            font-size: 1.2rem;
            box-shadow: 0 2px 8px rgba(52, 152, 219, 0.3);
        }
        
        .step-indicator strong {
            color: #1a252f !important;
            font-size: 1.2rem;
        }
        
        .step-indicator small {
            color: #34495e !important;
            font-size: 0.9rem;
        }
        
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border-radius: 12px !important;
            border: 2px solid #bdc3c7 !important;
            font-size: 16px !important;
            padding: 1rem !important;
            color: #2c3e50 !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #3498db !important;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2) !important;
        }
        
        .stButton > button {
            border-radius: 12px !important;
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%) !important;
            color: white !important;
            border: none !important;
            padding: 1rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4) !important;
        }
        
        .chat-message {
            background: linear-gradient(135deg, rgba(52, 152, 219, 0.1) 0%, rgba(52, 152, 219, 0.05) 100%);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 5px solid #3498db;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }
        
        .chat-message strong {
            color: #1a252f !important;
            font-size: 1.1rem;
        }
        
        .ai-response {
            background: linear-gradient(135deg, rgba(46, 204, 113, 0.1) 0%, rgba(46, 204, 113, 0.05) 100%);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 5px solid #2ecc71;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }
        
        .ai-response strong {
            color: #1a252f !important;
            font-size: 1.1rem;
        }
        
        .feature-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
        }
        
        .feature-item {
            background: rgba(255, 255, 255, 0.9);
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 5px solid #3498db;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease;
        }
        
        .feature-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
        }
        
        .feature-item strong {
            color: #1a252f !important;
            font-size: 1.1rem;
            display: block;
            margin-bottom: 0.5rem;
        }
        
        .vs-divider {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            color: #fff;
            margin: 3rem 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            background: linear-gradient(135deg, #e74c3c 0%, #3498db 50%, #2ecc71 100%);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .final-cta {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 3rem;
            border-radius: 20px;
            text-align: center;
            margin-top: 3rem;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.1);
        }
        
        .final-cta h2 {
            color: #fff !important;
            font-size: 2.2rem !important;
            margin-bottom: 1rem !important;
            text-shadow: none !important;
        }
        
        .final-cta h3 {
            color: #ecf0f1 !important;
            font-size: 1.6rem !important;
            margin-bottom: 1.5rem !important;
            text-shadow: none !important;
        }
        
        .final-cta p {
            color: #bdc3c7 !important;
            line-height: 1.6;
        }
        
        .animated-icon {
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-10px);
            }
            60% {
                transform: translateY(-5px);
            }
        }
        
        /* Streamlit specific overrides */
        .stExpander > div > div > div > div {
            background-color: rgba(255, 255, 255, 0.95) !important;
        }
        
        .stExpander label {
            color: #1a252f !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
        }
        
        .stSelectbox label {
            color: #1a252f !important;
            font-weight: 600 !important;
        }
        
        .stSelectbox > div > div > div {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border: 2px solid #bdc3c7 !important;
            border-radius: 12px !important;
        }
        
        .stDataFrame {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border-radius: 12px !important;
        }
        
        /* Make all text in dataframes more readable */
        .stDataFrame table {
            background-color: rgba(255, 255, 255, 0.98) !important;
        }
        
        .stDataFrame th {
            background-color: #34495e !important;
            color: white !important;
            font-weight: 600 !important;
        }
        
        .stDataFrame td {
            color: #2c3e50 !important;
        }
        
        /* Progress bar styling */
        .stProgress > div > div > div > div {
            background: linear-gradient(135deg, #3498db 0%, #2ecc71 100%) !important;
        }
        
        /* Success/Warning/Error message styling */
        .stSuccess {
            background-color: rgba(46, 204, 113, 0.15) !important;
            border-left: 5px solid #2ecc71 !important;
            border-radius: 10px !important;
        }
        
        .stWarning {
            background-color: rgba(241, 196, 15, 0.15) !important;
            border-left: 5px solid #f1c40f !important;
            border-radius: 10px !important;
        }
        
        .stError {
            background-color: rgba(231, 76, 60, 0.15) !important;
            border-left: 5px solid #e74c3c !important;
            border-radius: 10px !important;
        }
        
        .stInfo {
            background-color: rgba(52, 152, 219, 0.15) !important;
            border-left: 5px solid #3498db !important;
            border-radius: 10px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1>🧠 Field Force Intelligence – System of Work vs Traditional CRM</h1>
    <p style="text-align: center; font-size: 1.3rem; color: #34495e; margin-bottom: 0; font-weight: 500;">
        Experience the future of pharmaceutical field force management
    </p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for demo progression
if 'demo_step' not in st.session_state:
    st.session_state.demo_step = 0
if 'ai_responses' not in st.session_state:
    st.session_state.ai_responses = []

# Layout: Two side-by-side panels with better spacing
col1, col2 = st.columns([1, 1], gap="large")

# --- Left Panel: Traditional CRM Workflow --- #
with col1:
    st.markdown("""
    <div class="comparison-card traditional-card">
        <h2>📊 Traditional CRM Workflow</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 1: Filters and Target List
    with st.expander("🎯 Step 1: Manual Filtering & Target Lists", expanded=False):
        st.markdown("""
        <div class="step-indicator">
            <div class="step-number">1</div>
            <div>
                <strong>Login to CRM Dashboard</strong><br>
                <small>Navigate through multiple screens</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Simulate traditional workflow
        if st.button("🔍 Apply Filters", key="trad_filter"):
            with st.spinner("Loading CRM dashboard..."):
                time.sleep(2)
                st.success("Filters Applied:")
                st.code("""
Region: Bangalore South
Specialty: Cardiologist  
Last Visit: > 7 days
Territory: Zone-A
                """)
                
        if st.button("📥 Download Target List", key="trad_download"):
            with st.spinner("Generating Excel file..."):
                time.sleep(1.5)
                st.warning("⚠️ Excel file downloaded. Manual review required!")
                
                # Show sample data
                df = pd.DataFrame({
                    'Doctor Name': ['Dr. Mehta', 'Dr. Sharma', 'Dr. Patel'],
                    'Last Visit': ['12 days ago', '8 days ago', '15 days ago'],
                    'Specialty': ['Cardiologist', 'Cardiologist', 'Cardiologist'],
                    'Status': ['Active', 'Active', 'Active']
                })
                st.dataframe(df, use_container_width=True)

    # Step 2: Manual Planning
    with st.expander("📋 Step 2: Manual Planning & Preparation", expanded=False):
        st.markdown("""
        <div class="step-indicator">
            <div class="step-number">2</div>
            <div>
                <strong>Review & Plan Manually</strong><br>
                <small>Time-consuming analysis</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Manual Tasks Required:**
        - 📊 Check each doctor's prescription history
        - 📁 Find relevant sales materials
        - 🗺️ Plan route manually
        - 📝 Prepare generic talking points
        - 📧 Send bulk communications
        """)
        
        if st.button("⏱️ Simulate Manual Planning", key="manual_plan"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            steps = [
                "Reviewing doctor profiles...",
                "Checking prescription data...",
                "Finding sales materials...",
                "Planning route...",
                "Preparing talking points..."
            ]
            
            for i, step in enumerate(steps):
                status_text.text(step)
                progress_bar.progress((i + 1) / len(steps))
                time.sleep(0.8)
            
            st.error("⚠️ 25 minutes spent on manual preparation!")

    # Step 3: Limitations
    with st.expander("⚠️ Step 3: Limitations & Issues", expanded=False):
        st.markdown("""
        <div class="feature-list">
            <div class="feature-item">
                <strong>🐌 Slow Process</strong><br>
                Hours of manual work daily
            </div>
            <div class="feature-item">
                <strong>📊 Static Data</strong><br>
                No real-time insights
            </div>
            <div class="feature-item">
                <strong>🎯 Generic Approach</strong><br>
                One-size-fits-all messaging
            </div>
            <div class="feature-item">
                <strong>❌ No Context</strong><br>
                Missing conversation history
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- Right Panel: AI-Powered Field Force Intelligence --- #
with col2:
    st.markdown("""
    <div class="comparison-card ai-card">
        <h2>🤖 Field Force Intelligence (AI-Powered)</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 1: Natural Language Query
    with st.expander("💬 Step 1: Ask in Natural Language", expanded=True):
        st.markdown("""
        <div class="step-indicator">
            <div class="step-number">1</div>
            <div>
                <strong>Simply Ask What You Need</strong><br>
                <small>No complex navigation required</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        query = st.text_input(
            "🗨️ Ask your AI assistant:",
            placeholder="Who should I meet in Bangalore South today?",
            key="ai_query"
        )
        
        if query or st.button("🚀 Get Smart Recommendations", key="ai_rec"):
            if not query:
                query = "Who should I meet in Bangalore South today?"
                
            st.markdown(f'<div class="chat-message">👤 <strong>You:</strong> {query}</div>', unsafe_allow_html=True)
            
            with st.spinner("AI analyzing real-time data..."):
                time.sleep(1.5)
                
            st.markdown("""
            <div class="ai-response">
                🤖 <strong>AI Assistant:</strong><br><br>
                Based on real-time analysis, here are your top 3 priorities for today:
                <br><br>
                <strong>1. 🏥 Dr. Mehta (Cardiology)</strong><br>
                • Rising Telmisartan usage (+23% this month)<br>
                • Not visited in 12 days<br>
                • Previously showed interest in combination therapy<br>
                • <em>Best time: 10:30 AM (between surgeries)</em>
                <br><br>
                <strong>2. 🏥 Dr. Ramesh (Cardiology)</strong><br>
                • Competitor prescriptions spiking (+15%)<br>
                • Opportunity for counter-positioning<br>
                • Last meeting was positive<br>
                • <em>Best time: 2:00 PM (post-lunch rounds)</em>
                <br><br>
                <strong>3. 🏥 Dr. Anitha (Cardiology)</strong><br>
                • Responded positively to last presentation<br>
                • Ready for follow-up on Amlodipine switch<br>
                • High prescription volume potential<br>
                • <em>Best time: 4:30 PM (end of OPD)</em>
                <br><br>
                🗺️ <strong>Optimized route planned</strong> - Total travel time: 2.3 hours
            </div>
            """, unsafe_allow_html=True)

    # Step 2: Interactive Planning
    with st.expander("🎯 Step 2: Smart Planning & Insights", expanded=False):
        st.markdown("""
        <div class="step-indicator">
            <div class="step-number">2</div>
            <div>
                <strong>AI-Generated Insights</strong><br>
                <small>Real-time, contextual planning</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Sample map data
        if st.button("🗺️ Show Optimized Route", key="show_route"):
            # Create sample route visualization using Streamlit's built-in map
            map_data = pd.DataFrame({
                'lat': [12.9716, 12.9342, 12.9698],
                'lon': [77.5946, 77.6101, 77.5946],
            })
            
            st.map(map_data, zoom=11, use_container_width=True)
            
            # Show route details
            st.markdown("""
            <div class="ai-response">
                🗺️ <strong>Optimized Route Details:</strong><br><br>
                <strong>📍 Stop 1:</strong> Dr. Mehta (10:30 AM) - 15 min visit<br>
                <strong>📍 Stop 2:</strong> Dr. Ramesh (2:00 PM) - 20 min visit<br>  
                <strong>📍 Stop 3:</strong> Dr. Anitha (4:30 PM) - 25 min visit<br><br>
                <strong>🚗 Total Travel Time:</strong> 2.3 hours<br>
                <strong>⚡ Time Saved:</strong> 1.2 hours vs manual routing
            </div>
            """, unsafe_allow_html=True)
        
        # Show key insights
        col2a, col2b = st.columns(2)
        with col2a:
            st.markdown("""
            <div class="metric-card">
                <h3>⚡ Time Saved</h3>
                <h2>87%</h2>
                <p>vs manual planning</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2b:
            st.markdown("""
            <div class="metric-card">
                <h3>🎯 Success Rate</h3>
                <h2>94%</h2>
                <p>meeting acceptance</p>
            </div>
            """, unsafe_allow_html=True)

    # Step 3: Personalized Engagement
    with st.expander("🎨 Step 3: Personalized Pitch Generation", expanded=False):
        st.markdown("""
        <div class="step-indicator">
            <div class="step-number">3</div>
            <div>
                <strong>Custom Messaging</strong><br>
                <small>Tailored for each doctor</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        doctor_select = st.selectbox(
            "Select doctor for personalized pitch:",
            ["Dr. Mehta", "Dr. Ramesh", "Dr. Anitha"],
            key="doctor_select"
        )
        
        if st.button("🎯 Generate Personalized Pitch", key="gen_pitch"):
            with st.spinner("AI analyzing doctor's profile and history..."):
                time.sleep(1.2)
            
            if doctor_select == "Dr. Mehta":
                st.markdown("""
                <div class="ai-response">
                    🎯 <strong>Personalized Pitch for Dr. Mehta:</strong><br><br>
                    
                    <strong>Opening:</strong> "Dr. Mehta, I noticed your Telmisartan prescriptions have increased 23% this month - that shows excellent patient outcomes!"<br><br>
                    
                    <strong>Key Points:</strong><br>
                    • Reference his previous interest in combination therapy<br>
                    • Share new clinical data on adherence improvement<br>
                    • Address his past price concerns with value proposition<br><br>
                    
                    <strong>Supporting Data:</strong><br>
                    • 15% better adherence vs Brand X<br>
                    • Cost-per-outcome analysis ready<br>
                    • Patient case studies from similar demographics<br><br>
                    
                    <strong>Call-to-Action:</strong> Propose pilot program with 10 patients
                </div>
                """, unsafe_allow_html=True)
            
            col3a, col3b = st.columns(2)
            with col3a:
                if st.button("✅ Use This Pitch", key="use_pitch"):
                    st.success("✅ Pitch saved to your meeting agenda!")
            
            with col3b:
                if st.button("🔄 Generate Alternative", key="alt_pitch"):
                    st.info("🔄 Alternative pitch generated!")

    # Step 4: Real-time Tracking
    with st.expander("📊 Step 4: Real-time Impact Tracking", expanded=False):
        st.markdown("""
        <div class="step-indicator">
            <div class="step-number">4</div>
            <div>
                <strong>Live Performance Analytics</strong><br>
                <small>Continuous learning and optimization</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📈 Show Today's Impact", key="show_impact"):
            # Simulate real-time analytics
            col4a, col4b, col4c = st.columns(3)
            
            with col4a:
                st.markdown("""
                <div class="metric-card">
                    <h4>Doctors Met</h4>
                    <h2>5/5</h2>
                    <small>100% success rate</small>
                </div>
                """, unsafe_allow_html=True)
            
            with col4b:
                st.markdown("""
                <div class="metric-card">
                    <h4>Engagement Score</h4>
                    <h2>8.7/10</h2>
                    <small>Above average</small>
                </div>
                """, unsafe_allow_html=True)
            
            with col4c:
                st.markdown("""
                <div class="metric-card">
                    <h4>Est. Monthly Uplift</h4>
                    <h2>₹1.8L</h2>
                    <small>Based on commitments</small>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="ai-response">
                📊 <strong>Daily Summary & Insights:</strong><br><br>
                
                ✅ <strong>Completed Visits:</strong><br>
                • Dr. Mehta: Strong interest in combination therapy pilot<br>
                • Dr. Ramesh: Agreed to evaluate vs current competitor<br>
                • Dr. Anitha: Committed to 30-patient Amlodipine switch<br><br>
                
                🎯 <strong>Key Wins:</strong><br>
                • 2 doctors showed conversion interest<br>
                • 1 competitive displacement opportunity<br>
                • 3 follow-up meetings scheduled<br><br>
                
                🔮 <strong>AI Recommendations for Tomorrow:</strong><br>
                • Follow up with Dr. Mehta on pilot program details<br>
                • Prepare competitor comparison for Dr. Ramesh<br>
                • Schedule Dr. Anitha's patient transition timeline
            </div>
            """, unsafe_allow_html=True)