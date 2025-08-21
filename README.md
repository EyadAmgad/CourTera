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


## 📂 Project Structure

