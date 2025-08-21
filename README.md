# CourTera

This is a Django-based web application that allows users to explore courses, register/login, and leave reviews.  
The platform integrates a **Sentiment Analysis Model** that analyzes user reviews and generates a star rating (out of 5).

---

## 🚀 Features

### 🔑 Authentication
- User registration & login
- Secure logout
- User-specific course tracking (`My Courses`)

### 📘 Course Management
- Browse available courses
- Each course has:
  - Title
  - Cover image
  - Description
  - Direct link

### ⭐ Sentiment Analysis
- Users can leave text reviews on courses
- AI model predicts a **star rating (1-5)** from the review text
- Helps other users evaluate courses faster

### 👩‍💻 Admin Features
- Manage courses (add/update/delete)
- Manage users
- View reviews with auto-generated ratings

---

## ⚙️ Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **ML Model:** Sentiment analysis using BERT
- **Frontend:** HTML , CSS and JavaScript

---
.
├── build                   # Compiled files (alternatively `dist`)
├── docs                    # Documentation files (alternatively `doc`)
├── src                     # Source files (alternatively `lib` or `app`)
├── test                    # Automated tests (alternatively `spec` or `tests`)
├── tools                   # Tools and utilities
├── LICENSE
└── README.md
## 📂 Project Structure
Courtera/
│── courtera/ # App for managing courses
│ │── migrations/ # Database migrations
│ │── static/ # Static files (CSS, JS, images)
│ │── templates/ # HTML templates
│ │── admin.py # Django admin configuration
│ │── apps.py # App configuration
│ │── models.py # Database models
│ │── urls.py # App-specific URL routing
| │── utils.py # BERT model
│ │── views.py # App logic
│
│── mysite/ # Main Django project folder
│ │── settings.py # Project settings
│ │── urls.py # Root URL routing
│ │── wsgi.py # WSGI config
│ │── asgi.py # ASGI config
│
│
│── manage.py # Django project manager
│── requirements.txt # Python dependencies
│── README.md # Project documentation
