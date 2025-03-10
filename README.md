# Django Login API
A simple Django-based authentication API that uses JWT for secure login and token management.

## Features
- User authentication using JWT tokens
- Secure login endpoint
- Token refresh endpoint
- Django REST Framework integration
- Supports frontend authentication requests

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sylvester-exp/Login_API.git
   cd Login_API
2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies**
```bash
   pip install -r requirements.txt

   python manage.py migrate

   python manage.py runserver

## API Endpoints

| Method | Endpoint             | Description                          |
|--------|----------------------|--------------------------------------|
| `POST` | `/api/auth/login/`   | Logs in a user and returns JWT token |
| `POST` | `/api/auth/refresh/` | Refreshes the access token           |


## Usage Example

## Login Request (cURL)
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password": "admin"}'

## Environment Variables

```md
## Environment Variables

Create a `.env` file with:
SECRET_KEY='django-insecure-fv_1_(d4v%8qdr_@r1ow+)a-@gq-+9j35^2067a$=gqohb^ozk'
 DEBUG=True ALLOWED_HOSTS=127.0.0.1,localhost

## Deployment

The API is live at: http://127.0.0.1:8000

---

## Contributors & License
```md
## Contributors
- Abigail Sylvester (https://github.com/sylvester-exp)

## License
This project is open-source under the MIT License.



