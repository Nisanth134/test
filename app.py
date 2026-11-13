# app.py
from flask import Flask, render_template, request
from matcher import get_best_matches

app = Flask(__name__)

INTERNSHIPS_DB = [
    {"id": 1, "company": "Tech Corp", "role": "Backend Developer", "required_skills": ["python", "flask", "sql"]},
    {"id": 2, "company": "DataWorks", "role": "Data Analyst", "required_skills": ["python", "pandas", "excel"]},
    {"id": 3, "company": "Web Solutions", "role": "Frontend Intern", "required_skills": ["html", "css", "javascript", "bootstrap"]},
    {"id": 4, "company": "Cloud Sync", "role": "DevOps Intern", "required_skills": ["python", "linux", "aws", "docker"]}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    matches = []
    if request.method == 'POST':
        student_name = request.form.get('name')
        skills_input = request.form.get('skills', '')
        
        # Convert comma-separated string to list
        student_skills = [skill.strip() for skill in skills_input.split(',') if skill.strip()]
        student = {"name": student_name, "skills": student_skills}
        
        try:
            matches = get_best_matches(student, INTERNSHIPS_DB)
        except Exception as e:
            return f"An error occurred: {str(e)}", 400
            
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
