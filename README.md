# Student Internship Matching System

## Project Overview
A Python-based web application that matches students to open internships based on their skill sets. Built with Flask, tested with pytest, and deployed via Render.

## Live Demo
[Insert Render URL here once deployed]

## Setup Instructions (Local Development)
1. Clone the repository: `git clone <repo_url>`
2. Navigate to the folder: `cd internship-matching-system`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`
5. Open a browser and go to `http://127.0.0.1:5000`

## Automated Testing
This project uses `pytest` for automated testing. 
To run the tests locally, execute:
`pytest`
*(Note: Tests also run automatically on GitHub Actions on every push/PR to main).*

## Limitations
* Uses a mock, hard-coded database instead of a live database (e.g., PostgreSQL).
* Matching algorithm is basic and relies on exact string overlaps (case-insensitive).

## Team Contributions
* **Person 1:** Setup repository, GitHub Actions, implemented core backend algorithm (`matcher.py`), handled input validation and edge cases.
* **Person 2:** Wrote pytest suite (`test_matcher.py`), built the Flask web server (`app.py`), and designed the Bootstrap frontend (`index.html`).
* **Person 3:** Configured production server settings (`gunicorn`), wrote final documentation, and managed cloud deployment via Render.
