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