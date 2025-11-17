# SE Project Implementation Phase: Traffic Sign Recognition

This repository contains the complete implementation phase for our Software Engineering project. The project is a web application that uses a Flask backend to simulate traffic sign recognition from an image uploaded via a JavaScript frontend.

The project was built using an Agile Scrum methodology over two, one-week sprints and includes a full 5-stage CI/CD pipeline.

**Final Status:** ✅ Project Complete. All rubric requirements met.

---

## 🚀 Final Quality Scores (Rubric Met)

| Metric | Score | Rubric Requirement | Status |
| :--- | :--- | :--- | :--- |
| **Test Coverage** | **86%%** | `>= 75%` | ✅ **Pass** |
| **Lint Score** | **8.12 / 10** | `>= 7.5` | ✅ **Pass** |
| **Security Scan** | **Pass** | `Scan must run` | ✅ **Pass** |
| **Unit/Integration Tests**| **6 / 6 Passed** | `All tests pass` | ✅ **Pass** |
| **CI/CD Pipeline** | **5 Stages + Artifact** | `All stages pass` | ✅ **Pass** |

---

## ⚙️ How to Run Locally

You must run two separate servers (backend and frontend) in two separate terminals.

### 1. Backend (Flask)

```bash
# 1. Go to the backend folder
cd backend

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask server
python app.py
```
Backend will be running at http://127.0.0.1:5000

### 2. Frontend (HTTP Server)

```# (In a new terminal)
# 1. Go to the frontend folder
cd frontend

# 2. Start a simple Python web server
python3 -m http.server 5500
```
Open your browser and go to http://127.0.0.1:5500/
🧪 Testing & CI/CD Pipeline
This project is configured with a full 5-stage CI/CD pipeline using GitHub Actions, as required by the rubric.

1. How to Run Tests Locally
```
# 1. Activate your virtual environment
source venv/bin/activate

# 2. Install testing dependencies
pip install pytest pytest-cov pylint bandit

# 3. Run all tests
pytest -q

# 4. Check Test Coverage (Goal: >75%)
pytest --cov=backend

# 5. Check Pylint Score (Goal: >7.5)
pylint backend/app.py

# 6. Run Security Scan
bandit -r backend
```
2. Automated CI/CD Pipeline Stages
Our pipeline (defined in .github/workflows/ci.yml) automatically runs on every Pull Request.

Build: Installs all Python dependencies from requirements.txt.

Test: Runs all 6 pytest tests (unit, integration, and error-path).


Lint: Runs pylint on the backend and fails the build if the score is < 7.5. 



Coverage: Runs pytest-cov and fails the build if test coverage is < 75%. 



Security: Runs bandit to scan for vulnerabilities and saves the report. 


3. Deployment Artifact (Final Submission)
After all 5 stages pass on the main branch, a final job runs:


Deploy: This job bundles all source code (backend/, frontend/), documentation (README.md, docs/), and all CI reports (htmlcov/, bandit-report.txt, pylint-report.txt) into a single deployment-package.zip file, which is then uploaded as an artifact for submission .


### Sprint Summary
Sprint 1: Core Implementation
Goal: Build the basic end-to-end connection.

Outcome: Successfully connected the frontend UI to the Flask backend. Solved all major CORS and fetch bugs.

Sprint 2: Quality & Automation (Rubric Requirements)
Goal: Meet all rubric requirements for CI/CD, Testing, and Quality.

Outcome: Successfully built the 5-stage pipeline, achieved 95% coverage, passed all lint/security checks, and produced a final deployment-package.zip artifact.
