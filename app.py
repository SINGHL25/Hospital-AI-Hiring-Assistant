
import streamlit as st
import os
from PyPDF2 import PdfReader
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Hospital AI Hiring Assistant")
st.title("🏥 AI Hiring Assistant - Hospital HR")

st.subheader("📝 Generate a Job Description (JD)")
job_title = st.text_input("Enter Job Title (e.g., Nurse, Radiologist, Receptionist)")

if st.button("Generate JD"):
    with st.spinner("Generating with AI..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Write a professional job description for the role of {job_title} in a basic hospital setup."}
            ]
        )
        jd = response.choices[0].message.content
        st.text_area("Generated Job Description", jd, height=300)

st.subheader("📥 Upload Resume for Screening")
uploaded = st.file_uploader("Upload a Resume (PDF only)", type="pdf")

if uploaded:
    reader = PdfReader(uploaded)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()

    st.text_area("Resume Content (Extracted)", resume_text[:3000], height=250)

    if st.button("Match Resume to JD"):
        prompt = f"""
You are an HR agent. Compare this job description and resume, and return a match score out of 100. No extra explanation.

Job Description:
{jd}

Resume:
{resume_text}
"""

        with st.spinner("Scoring with AI..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            score = response.choices[0].message.content.strip()
            st.success(f"✅ Resume Match Score: {score}")
