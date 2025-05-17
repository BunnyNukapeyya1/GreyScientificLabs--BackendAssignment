
# 🏥 Hospital Management System - Django Backend

A RESTful API built with Django to manage doctors, patients, and medical records with secure access and authentication.

---

## 🚀 Live API

🌐 **Deployed at:** [https://hospital-management-qwg9.onrender.com](https://hospital-management-qwg9.onrender.com)

---

## 📦 Features

- 👨‍⚕️ Doctor Signup & Token-based Login
- 🧑‍🤝‍🧑 Add/View Patients (Doctor access only)
- 📝 Add/View Medical Records (linked to Patients)
- 🔐 Custom permissions to restrict data access



## 🛠 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/BunnyNukapeyya1/GreyScientificLabs--BackendAssignment
cd GreyScientificLabs--BackendAssignment
````

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (optional)

```bash
python manage.py createsuperuser
```

---

## ▶ Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and visit:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Running Tests

To run the full test suite:

```bash
python manage.py test
```

---

## 🔐 Authentication

This project uses **Token Authentication**.

1. Login via the `/login` endpoint with valid credentials.
2. Copy the token returned in the response.
3. Include the token in the header for all protected requests:

```
Authorization: Token your_token_here
```

---

## 📬 API Endpoints

| Method | Endpoint                             | Description                             |
| ------ | ------------------------------------ | --------------------------------------- |
| POST   | `/api/signup`                            | Register a new doctor                   |
| POST   | `/api/login`                             | Login and receive an auth token         |
| POST   | `/api/patients`                          | Create a patient (Doctors only)         |
| GET    | `/api/patients/all`                      | View patients added by logged-in doctor |
| POST   | `/api/patients/records/add`              | Add a medical record to a patient       |
| GET    | `/api/patients/<int:patient_id>/records` | Get records for a specific patient      |

---


