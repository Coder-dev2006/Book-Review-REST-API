# 📚 Book Review REST API

A RESTful API built with **Django REST Framework** that allows users to browse books, leave reviews, and manage data securely.  
This project demonstrates solid backend design with authentication, nested routing, and clean, maintainable code.

---

## 🚀 Features

✅ User Authentication (Login / Logout via DRF Session Auth)  
✅ CRUD operations for Books and Reviews  
✅ Nested API endpoints (Books → Reviews)  
✅ Average rating calculation for each book  
✅ Admin panel for managing data  
✅ Permissions for safe access  
✅ Well-structured Django apps (books, users)

---

## 🧩 Tech Stack

- **Python 3.10+**
- **Django 4+**
- **Django REST Framework (DRF)**
- **DRF Nested Routers**
- **SQLite (default)**

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/book-review-api.git
cd book-review-api
2️⃣ Create and activate a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5️⃣ Create a superuser
bash
Copy code
python manage.py createsuperuser
6️⃣ Start the development server
bash
Copy code
python manage.py runserver
🌐 API Endpoints
Method	Endpoint	Description
GET	/api/books/	List all books
POST	/api/books/	Add a new book (admin only)
GET	/api/books/{id}/	Retrieve single book
GET	/api/books/{id}/reviews/	Get all reviews for a book
POST	/api/books/{id}/reviews/	Add a review (authenticated users)
GET	/api/auth/login/	Login
GET	/api/auth/logout/	Logout

🔐 Authentication
This project uses Session Authentication (default DRF login).
You can log in from:

arduino
Copy code
http://127.0.0.1:8000/api/auth/login/
Then, test authenticated endpoints directly in the DRF web interface.

📊 Example JSON Response
json
Copy code
[
  {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "description": "The classic book about writing clean and maintainable code.",
    "created_at": "2025-10-15T17:40:20Z",
    "avg_rating": 5.0,
    "reviews": [
      {
        "id": 1,
        "user": "admin",
        "rating": 5,
        "comment": "A must-read for every developer!",
        "created_at": "2025-10-15T18:02:45Z"
      }
    ]
  }
]
🧠 Project Structure
bash
Copy code
book_review_api/
├── book_review_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── books/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
└── users/
    ├── models.py
    ├── views.py
    ├── serializers.py
👨‍💻 Author
Samandar Fayziyev
Junior Python Developer | Django & REST API 
https://github.com/Coder-dev2006

🏁 Future Improvements
🔐 Add JWT Authentication

🧾 Add Swagger documentation

🧮 Add Pagination and Filtering

🐳 Add Docker support for deployment

📜 License
This project is open-source and available under the MIT License.

**👉 I will add more updates to this project soon**
