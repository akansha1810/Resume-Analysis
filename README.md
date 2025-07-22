# Resume-Analysis

###STeps for creating the project 
1. Create the virtual enviornment
2. Avtivate the vortual enviornment using ``source.venv/Scripts/activate``
3. create the .env file to store the API Key
4. Create the requirements.txt file and add the libraries for installation
using ``pip install -r requirements.txt``


### Project SYnopsis
we want to create a application that will analyse the resume of the candidate using GenAI model
with the job description and provide insights such as :-
- ATS SCores
- Probability of getiing hired
- Keyword analysis
- SWOT analysis
- Suggestions for overall improvements

### Architecture 
* app.py : front end creation and output off GEnai Model 
* It will have the feature of capturing information such as Resume and JD
* Information we are capturing is resume.pdf and Job Description 
* pdf.py that will process the information in pdf and that's why we installed ``pypdf``
* analysis.py that will triangulate the pdf information and the JD and will provide insights and next step.



# 📄 Resume Analysis App (CV.ai)

**Live Demo**: [https://resume-analysis-ekhyq7ct333kqhtprcgks6.streamlit.app](https://resume-analysis-ekhyq7ct333kqhtprcgks6.streamlit.app)

A smart AI-powered Streamlit web application that compares candidate resumes against job descriptions (JD) to generate an intelligent match score, skill gap analysis, and detailed insights. Built for recruiters, job seekers, and talent acquisition professionals.

---

## 🚀 Features

- ✅ Upload PDF resume and job description
- ✅ Extract and parse key skills, experiences, and education
- ✅ Match score between Resume & JD
- ✅ Highlight missing skills
- ✅ Natural language-based skill extraction using NLP
- ✅ Clean and interactive UI with Streamlit
- ✅ Deployed on **Streamlit Cloud**

---

## 📌 Use Case

This app helps:
- **Job Seekers** optimize their resumes for specific job roles
- **Recruiters** evaluate resume-job alignment instantly
- **Career Coaches** provide feedback using AI-driven comparison

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| 👩‍💻 Programming | Python 3.10+ |
| 🌐 Frontend UI | Streamlit |
| 📄 Parsing Engine | `PyPDF2`, `pdfminer.six`, or similar |
| 🧠 NLP & Analysis | `spaCy`, `nltk`, or custom logic |
| 📦 Deployment | Streamlit Cloud |
| 📊 Visualization | Streamlit widgets, metrics |

---

## 📂 Project Structure

