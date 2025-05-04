# 🏥 Hospital Management System - Django Backend

A RESTful API built with Django to manage doctors, patients, and medical records with secure access and authentication.

## 🚀 Live API

🌐 [https://hospital-management-qwg9.onrender.com](https://hospital-management-qwg9.onrender.com)

---

## 📦 Features

- Doctor Signup & Token-based Login
- Add/View Patients (Doctor access only)
- Add/View Medical Records (linked to Patients)
- Custom permissions to restrict data access

---

## 🛠 Getting Started

### 1. Clone the Repository

bash
git clone https://github.com/your-username/hospital-management.git
cd hospital-management


### 2. Create a Virtual Environment

bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate


### 3. Install Requirements

bash
pip install -r requirements.txt


---

## 🧪 Running Tests

Run all test cases using:

bash
python manage.py test


---

## ▶ Running Development Server

To start the local server:

bash
python manage.py runserver


Then open in your browser:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Authentication

This project uses **Token Authentication**.

After logging in via `/login`, use the returned token in headers for other requests:


Authorization: Token your_token_here


---

## 📬 API Endpoints

| Method | Endpoint                             | Description                             |
|--------|--------------------------------------|-----------------------------------------|
| POST   | `/signup`                            | Register a new user                     |
| POST   | `/login`                             | Login and receive an auth token         |
| POST   | `/patients`                          | Create a patient (Doctors only)         |
| GET    | `/patients/all`                      | View patients added by logged-in doctor |
| POST   | `/patients/records/add`              | Add medical record to a patient         |
| GET    | `/patients/<int:patient_id>/records` | Get records for a specific patient      |

---

