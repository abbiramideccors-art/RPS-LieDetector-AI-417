import streamlit as st
st.set_page_config(page_title="Lie Detector AI", layout="wide", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #1F4E79;'>LIE DETECTOR AI - Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>RPS Class X AI Project 2026-27 | Subject Code: 417</p>", unsafe_allow_html=True)
st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("Total Tests Run", "40", "8 new")
col2.metric("Model Accuracy", "75%", "2%")
col3.metric("Active Model", "Decision Tree")
st.divider()
c1, c2 = st.columns([2,1])
with c1:
    st.subheader("Upload & Analyze")
    st.file_uploader("Upload video clip", type=['mp4','mov'])
    st.button("▶️ Record Live", type="primary", use_container_width=True)
with c2:
    st.subheader("Live Prediction")
    st.success("Result: Likely Truthful")
    st.progress(82, text="Confidence: 82%")
st.caption("Note: This system detects stress indicators for educational purposes only, not actual lies.")

