# Django Blog Project

Welcome to the **Django Blog Project**, a web application for creating, editing, and publishing blog posts. This project demonstrates the use of Django for building a fully functional blogging platform.

---

## Features

- User authentication for login, registration, and password management.
- Create, edit, and delete blog posts.
- Commenting system for posts.
- Responsive design for seamless use on desktop and mobile devices.
- Admin interface for managing content.

---

## Installation Guide

### Prerequisites

Before you begin, ensure you have the following installed:

1. **Python (3.8 or later)**: [Download here](https://www.python.org/downloads/)
2. **pip**: Python's package manager (usually bundled with Python).
3. **Virtualenv** (optional but recommended): For creating isolated environments.

### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/nitin099/Blog-Fulfil.io-Assignment.git
   ```

2. **Set Up a Virtual Environment**:

   #### For Windows
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   #### For macOS/Linux
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

Access the application in your web browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).
