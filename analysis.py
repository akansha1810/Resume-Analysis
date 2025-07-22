import google.generativeai as genai
from pdf import process_pdf
import streamlit as st
import os 
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# Model setup
model = genai.GenerativeModel("gemini-1.5-flash")  # Good for PDFs

def analyse_profile(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf = process_pdf(pdf_doc)
        st.sidebar.markdown("✅ Uploaded Successfully")

        good_fit = model.generate_content(
            f'''Compare the job description: {job_desc} with the resume: {pdf} and suggest if I am a good fit for the role.'''
        )

        ats_score = model.generate_content(
            f'''Compare the job description: {job_desc} with the resume: {pdf} and suggest the ATS Score of the resume.'''
        )

        probability = model.generate_content(
            f'''Compare the job description: {job_desc} with the resume: {pdf} and suggest the Probability of getting selected (in %).'''
        )

        keywords = model.generate_content(
            f'''Compare the job description: {job_desc} with the resume: {pdf} and list the keywords from the job description missing in the resume.'''
        )

        swot = model.generate_content(
            f'''Compare the job description: {job_desc} with the resume: {pdf} and provide a SWOT analysis followed by actionable insights in bullet points.'''
        )

        projects = model.generate_content(
            f'''Compare the job description: {job_desc} with the resume: {pdf} and suggest relevant ML competitions or projects along with chances of selection (in %).'''
        )

        return (
            st.write(good_fit.text),
            st.write(ats_score.text),
            st.write(probability.text),
            st.write(keywords.text),
            st.write(swot.text),
            st.write(projects.text)
        )

    else:
        st.warning("📝 Please upload your resume to proceed.")
        return