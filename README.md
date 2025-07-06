# Hospital-AI-Hiring-Assistant
🏥 Hospital-AI-Hiring-Assistant
An AI-powered hiring assistant built with Streamlit and OpenAI GPT to automate job description creation, resume parsing, and candidate scoring for hospitals or clinics with basic to moderate operations.
Ideal for small to mid-sized healthcare facilities hiring staff like nurses, technicians, clerks, and assistants.

🔍 Features
Feature	Description
📄 Job Description Generator	Auto-generate job descriptions using OpenAI
📥 Resume Upload	Upload candidate resumes in PDF format
📊 JD-Resume Scoring	AI evaluates match between JD and resume
🔒 Secure	Uses OpenAI API key securely via .env

📁 Folder Structure
bash
Copy
Edit
hospital_ai_hiring_assistant/
├── main.py                 # Main Streamlit App
├── .env.sample             # Environment variable template
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation
🚀 Quick Start
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourname/hospital_ai_hiring_assistant.git
cd hospital_ai_hiring_assistant
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set Up OpenAI API Key
Copy .env.sample to .env:

bash
Copy
Edit
cp .env.sample .env
Add your OpenAI API key:

env
Copy
Edit
OPENAI_API_KEY=your-real-api-key-here
4. Run the App
bash
Copy
Edit
streamlit run main.py
📸 Demo Features
📝 JD Generation: Instant JD creation from a job title.

📄 Resume Parsing: Extract text from uploaded PDF.

🧠 Scoring: Get a match score out of 100 based on relevance.

🛠️ Built With
Streamlit

OpenAI GPT-3.5 API

PyPDF2

dotenv

📬 Example Use Case
“I want to hire a Lab Technician. I enter the job title, generate a JD, upload the resume of a candidate, and instantly see a relevance score. Saves hours of manual screening.”

🌐 Future Features (Suggestions)
Store shortlists to database (e.g., Firebase or MongoDB)

Add AI-based cover letter generator

Send shortlisted resumes via email

Interview Q&A generator using GPT

👤 Author
Akhilesh Kumar Singh
Email: akhi.singh1989@gmail.com
Location: Varanasi, Uttar Pradesh, India

