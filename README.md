{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # \uc0\u55357 \u56998  SE Project Implementation Phase \'96 Traffic Sign Recognition\
\
### \uc0\u55358 \u56800  Overview\
This repository contains the implementation phase of the **Software Engineering Project**, demonstrating a full Agile lifecycle using **Scrum**, **Flask**, and **Frontend\'96Backend integration**.\
\
### \uc0\u55356 \u57303 \u65039  Architecture\
- **Frontend:** HTML + CSS + JavaScript (image upload interface)\
- **Backend:** Flask API (`/predict`) with mock prediction response\
- **Testing:** pytest unit tests + pylint for linting\
- **Version Control:** Git + GitHub feature branch workflow\
- **Deployment:** Local environment (will add CI/CD in Sprint 2)\
\
### \uc0\u55358 \u56809  Features Implemented (Sprint 1)\
1. Frontend upload UI with validation\
2. Flask backend for image upload and mock prediction\
3. End-to-end integration verified\
4. Enabled CORS for local testing\
5. Added unit tests and code quality checks\
6. GitHub Actions pipeline drafted (for Sprint 2)\
\
### \uc0\u9881 \u65039  Setup & Run\
**Backend**\
```bash\
cd backend\
python3 -m venv venv\
source venv/bin/activate\
pip install -r requirements.txt\
python app.py\
}