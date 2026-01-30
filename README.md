# CodeVirtus - Road Safety Risk Assessment System

## 🔧 Backend Setup & Database Documentation

### Prerequisites
* Python 3.10+
* PostgreSQL (Optional for local dev, required for production)

### 🚀 Installation
1. **Clone the repository**
   ```bash
   git clone [https://github.com/elyzadeveraturda/CodeVirtus.git](https://github.com/elyzadeveraturda/CodeVirtus.git)
   cd CodeVirtus

2. **Create & Activate Virtual Environment**
    Windows:
        python -m venv venv
        venv\Scripts\activate

    Mac/Linux:
        python3 -m venv venv
        source venv/bin/activate    

3. **Install Dependencies**
    pip install -r requirements.txt


### 🗄️ Database Configuration
Current Status: Default SQLite (Development Mode)

The project is currently configured to use SQLite for local development. This allows the backend to run immediately without requiring external server credentials. The system is pre-configured (settings.py) to switch to PostgreSQL once production credentials are added to the .env file.

**To Initialize the Database:**

python manage.py makemigrations
python manage.py migrate

**Running the Server**
python manage.py runserver
    * API Root: http://127.0.0.1:8000/
    * Admin Panel: http://127.0.0.1:8000/admin/


### 🔐 Authentication & Security
**The API is secured with JWT (JSON Web Tokens).**
Most endpoints (e.g., `/api/accidents/reports/`) are locked and require a valid token.

**How to Authenticate (Login):**
1. Send a `POST` request to: `http://127.0.0.1:8000/api/token/`
2. Body: `{"username": "your_admin_user", "password": "your_password"}`
3. Response: You will receive an `access` token.
4. Use this token in the header of future requests:
   `Authorization: Bearer <your_access_token>`

### ⚙️ Running the Server
```bash
python manage.py runserver