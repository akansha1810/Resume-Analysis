from dotenv import load_dotenv
load_dotenv()  # Load the local variables
import streamlit as st
from pdf import process_pdf
from analysis import analyse_profile

# Create the front end of the application here...
st.header("ResumeIQ: :blue[Get Job-Ready Instantly📝]", divider = "green")
st.subheader("Tips for using the Application")

notes = f'''
* ** Upload the resume (pdf only):** Please upload the resume in pdf format only.
* **Paste the Job Description:** Copy paste teh Job Description below.
* Unleash the Power of LLMs:** Use the power of LLMs to derive insights about the resume.'''

st.write(notes)

#sidebar
st.sidebar.subheader("Upload the Resume")
pdf_doc = st.sidebar.file_uploader("Upload the Resume",type=["pdf"])
st.sidebar.write("Created by Akansha")

# Job Description Text Box
st.subheader("Enter the Job Description", divider = True)
job_desc = st.text_area(label="Enter the Job Description from Job Board(e.g. Lnkedin)",
             max_chars=10000)
submit = st.button(label="Get AI Powered Insights")

if submit:
    st.markdown(analyse_profile(pdf_doc=pdf_doc, job_desc=job_desc))