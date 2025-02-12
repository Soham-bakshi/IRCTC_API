# IRCTC API

This project is a **Flask-based API** for an IRCTC-like train booking system, integrated with **MySQL** for user authentication, train management, and ticket booking.

## **Features Implemented**
1. **User Registration & Login (JWT Authentication)**
2. **Train Management (Admin)**
3. **Seat Availability Check**
4. **Seat Booking**
5. **Fetch Booking Details**
6. **Database Management with MySQL & Flask-SQLAlchemy**

---
## **Setup Instructions**

### **1. Install Dependencies**
Ensure you have Python and MySQL installed, then install required Python packages:

```sh
pip install flask flask_sqlalchemy flask_bcrypt flask_jwt_extended pymysql flask_migrate python-dotenv
```

### **2. Database Configuration (MySQL)**
1. Open MySQL and create a database:
   ```sql
   CREATE DATABASE irctc_db;
   ```
2. Update the `config.py` file with the MySQL connection details:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()

   class Config:
       SQLALCHEMY_DATABASE_URI = "mysql+pymysql://soham:soham123@localhost/irctc_db"
       JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY","24dd80b83e54bfabd5e777ef97bb79fd35a51965cae12cfaebbdfdc00a390f94" 
")
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

### **3. Initialize the Database**
Run the following commands to apply migrations and create tables:

```sh
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

---
## **API Endpoints**

### **1️⃣ User Authentication**
#### **Register a New User**
```sh
curl -X POST "http://127.0.0.1:5000/auth/register" \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "1234"}'
```
#### **Login to Get JWT Token**
```sh
curl -X POST "http://127.0.0.1:5000/auth/login" \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "1234"}'
```
Response:
```json
{"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczOTM0MTQyMCwianRpIjoiYzYwYWYzYWQtOGQyMy00ZjkzLTg4NTgtMWMxZjBmMTc2YzE1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwidXNlcm5hbWUiOiJ0ZXN0dXNlciIsInJvbGUiOiJ1c2VyIn0sIm5iZiI6MTczOTM0MTQyMCwiY3NyZiI6IjMzNThlNjI3LWQ1MzMtNDYyMC04YTE2LTA5MzAwMjU3OWRlMCIsImV4cCI6MTczOTM0MjMyMH0.TKATc85pp5d66sYU7yP5fRQS8tXAj7ZYWPg7AeUniJA
"}
```

---
### **2️⃣ Admin - Manage Trains**
#### **Add a New Train** (Admin Only)
```sh
curl -X POST "http://127.0.0.1:5000/admin/trains" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczOTM0MTQyMCwianRpIjoiYzYwYWYzYWQtOGQyMy00ZjkzLTg4NTgtMWMxZjBmMTc2YzE1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwidXNlcm5hbWUiOiJ0ZXN0dXNlciIsInJvbGUiOiJ1c2VyIn0sIm5iZiI6MTczOTM0MTQyMCwiY3NyZiI6IjMzNThlNjI3LWQ1MzMtNDYyMC04YTE2LTA5MzAwMjU3OWRlMCIsImV4cCI6MTczOTM0MjMyMH0.TKATc85pp5d66sYU7yP5fRQS8tXAj7ZYWPg7AeUniJA
" \
-d '{"train_name": "Express 101", "source": "Mumbai", "destination": "Delhi", "total_seats": 100}'
```

---
### **3️⃣ User - Train Search & Booking**
#### **Check Seat Availability**
```sh
curl -X GET "http://127.0.0.1:5000/user/trains?source=Mumbai&destination=Delhi" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczOTM0MTQyMCwianRpIjoiYzYwYWYzYWQtOGQyMy00ZjkzLTg4NTgtMWMxZjBmMTc2YzE1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwidXNlcm5hbWUiOiJ0ZXN0dXNlciIsInJvbGUiOiJ1c2VyIn0sIm5iZiI6MTczOTM0MTQyMCwiY3NyZiI6IjMzNThlNjI3LWQ1MzMtNDYyMC04YTE2LTA5MzAwMjU3OWRlMCIsImV4cCI6MTczOTM0MjMyMH0.TKATc85pp5d66sYU7yP5fRQS8tXAj7ZYWPg7AeUniJA
"
```

#### **Book a Seat**
```sh
curl -X POST "http://127.0.0.1:5000/user/book" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_JWT_TOKEN" \
-d '{"train_id": 1}'
```

#### **Get Booking Details**
```sh
curl -X GET "http://127.0.0.1:5000/user/bookings" \
-H "Authorization: Bearer YOUR_JWT_TOKEN"
```

---
## **Running the Flask App**
Start the Flask server:
```sh
python app.py
```
The API will be available at: `http://127.0.0.1:5000/`

---
## **Database Tables (MySQL)**
Run the following command in MySQL to check tables:
```sql
SHOW TABLES;
```
Expected tables:
- `users`
- `trains`
- `bookings`

---
## **Troubleshooting**
- **Flask App Not Running?**
  ```sh
  export FLASK_APP=app.py
  flask run
  ```
- **Database Connection Issues?**
  ```sh
  mysql -u root -p
  GRANT ALL PRIVILEGES ON irctc_db.* TO 'soham'@'localhost' IDENTIFIED BY 'soham123';
  ```
- **JWT Token Expired?** Re-login to get a new one.

---
## **Author**
Developed by **Soham Bakshi** 🚀

