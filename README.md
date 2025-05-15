📌 Overview
This is a Django REST Framework (DRF) based backend for a Candidate Management System (CMS).
It provides APIs to manage Candidates and Tasks with Token Authentication.

🚀 Features
Candidate CRUD APIs
Task CRUD APIs
DRF Browsable API
Token Authentication
Django Admin Panel

🛠 Technologies Used
Python 3
Django 5.x
Django REST Framework (DRF)
SQLite (Default Database)


⚙️ Setup Instructions
Clone the repository or extract the project folder.

Navigate to the project directory:

bash
Copy
Edit
cd cms_backend
Install the dependencies:

nginx
Copy
Edit
pip install -r requirements.txt
Apply migrations:

nginx
Copy
Edit
python manage.py migrate
Run the development server:

nginx
Copy
Edit
python manage.py runserver
📂 API Endpoints (via DRF Router)
Endpoint	Description
/api/candidates/	Manage Candidates
/api/tasks/	Manage Tasks
/api-auth/	DRF Login/Logout
Each supports GET, POST, PUT, PATCH, DELETE operations based on the method.

🔐 Admin Panel
Access the Django admin panel at:

arduino
Copy
Edit
http://127.0.0.1:8000/admin/
Create a superuser to access admin:

nginx
Copy
Edit
python manage.py createsuperuser
📄 License
This project is for learning and practice purposes.