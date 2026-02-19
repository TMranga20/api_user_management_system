@"
# 🚀 ReqRes API - User Management System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-API%20Testing-green)
![API Automation](https://img.shields.io/badge/API-Automation-red)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange)
![Report](https://img.shields.io/badge/Report-pytest--html-red)
![Status](https://img.shields.io/badge/Tests-Passing-brightgreen)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

A production-style API - User Management System built using Python, Pytest, and Requests to validate CRUD operations on the ReqRes User Management API.

---

## 📌 Features

✔ CRUD API automation (Create, Read, Update, Delete)  
✔ API key authentication using environment variables  
✔ Reusable API client with common request handler  
✔ Request & response logging for debugging  
✔ HTML test execution report generation  
✔ Clean GitHub-ready project structure  

---

## 🛠 Tech Stack

- Python  
- Pytest  
- Requests  
- pytest-html  
- Git & GitHub  

---

## 📂 Project Structure

api_user_management/
├── tests/

├── utils/

├── reports/

├── conftest.py

├── pytest.ini

├── requirements.txt

└── README.md

---

## 🔐 Setup API Key

Get your free key: https://app.reqres.in/api-keys

Windows:
setx REQRES_API_KEY "your_api_key_here"

Mac/Linux:
export REQRES_API_KEY="your_api_key_here"

Restart terminal after setting.

---

## ▶️ How to Run Tests

pip install -r requirements.txt  
pytest  

---

## 📊 Generate HTML Report

pytest --html=reports/api_report.html --self-contained-html

Report location: reports/api_report.html

---

## ✅ Test Coverage

Create User → POST /users → 201  
Get User → GET /users/{id} → 200  
Update User → PUT /users/{id} → 200  
Delete User → DELETE /users/{id} → 204  

---

## 🎯 Key Learning Outcomes

- API automation using Pytest  
- Authentication handling with headers  
- Environment variable management  
- Reusable request abstraction  
- Debug logging for failures  
- Professional reporting  

---

## 👨‍💻 Author

Mohan Ranga  
QA Tester 

If you like this project, star the repository ⭐
