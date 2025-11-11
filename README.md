# 🚦 SE Project Implementation Phase – Traffic Sign Recognition

### 🧠 Overview
This repository contains the implementation phase of the **Software Engineering Project**, demonstrating a full Agile lifecycle using **Scrum**, **Flask**, and **Frontend–Backend integration**.

### 🏗️ Architecture
- **Frontend:** HTML + CSS + JavaScript (image upload interface)
- **Backend:** Flask API (`/predict`) with mock prediction response
- **Testing:** pytest unit tests + pylint for linting
- **Version Control:** Git + GitHub feature branch workflow
- **Deployment:** Local environment (will add CI/CD in Sprint 2)

### 🧩 Features Implemented (Sprint 1)
1. Frontend upload UI with validation
2. Flask backend for image upload and mock prediction
3. End-to-end integration verified
4. Enabled CORS for local testing
5. Added unit tests and code quality checks
6. GitHub Actions pipeline drafted (for Sprint 2)

### ⚙️ Setup & Run
**Backend**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
## 🧪 Testing & CI/CD
- Run tests: `pytest -v`
- Run lint: `pylint backend/app.py`
- GitHub Actions automatically runs these checks on every pull request.
