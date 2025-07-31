import streamlit as st
from scanner import VulnerabilityScanner
from gpt_integration import GPTIntegration
from ml_model import VulnScoringModel
import pandas as pd
import time
import plotly.express as px

import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("static/styles.css")

# App config
st.set_page_config(
    page_title="AI Pentest Tool",
    page_icon="🔒",
    layout="wide"
)

# Sidebar controls
st.sidebar.title("Settings")
target = st.sidebar.text_input("Target", "example.com")
scan_type = st.sidebar.selectbox("Scan Type", ["web", "api", "full"])
action = st.sidebar.button("Run Scan")

# Main app
st.title("AI-Powered Penetration Testing")
st.markdown("Automated vulnerability assessment with ML scoring and GPT analysis")

if action:
    with st.spinner("Running scan..."):
        # Run scan
        scanner = VulnerabilityScanner()
        results = scanner.run_nmap(target, scan_type)
        
        # Score vulnerabilities
        model = VulnScoringModel()
        df = pd.DataFrame(results)
        scored_df = model.score_vulnerabilities(df)
        
        # Generate report
        gpt = GPTIntegration()
        report = gpt.generate_report(scored_df.to_dict())
    
    # Display results
    st.subheader("Scan Results")
    st.dataframe(scored_df)
    
    st.subheader("Vulnerability Distribution")
    fig = px.pie(scored_df, names='severity', title='Vulnerability Severity')
    st.plotly_chart(fig)
    
    st.subheader("AI Analysis Report")
    st.markdown(report)
    
    # Export options
    st.download_button(
        label="Download Report",
        data=report,
        file_name=f"pentest_report_{target}.md",
        mime="text/markdown"
    )
