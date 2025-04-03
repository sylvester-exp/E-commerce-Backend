# 🛡️ Django Login API

A simple Django-based authentication API that uses JWT for secure login and token management.

## ✨ Features

- User authentication using JWT tokens
- Secure login endpoint
- Token refresh endpoint
- Django REST Framework integration
- Supports frontend authentication requests
- 📦 Homepage API with product listing, filtering, searching, and pagination

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sylvester-exp//E-commerce-Backend.git
   cd E-commerce-Backend
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## 🔐 Authentication API Endpoints

| Method | Endpoint             | Description                          |
|--------|----------------------|--------------------------------------|
| POST   | `/api/auth/login/`   | Logs in a user and returns JWT token |
| POST   | `/api/auth/refresh/` | Refreshes the access token           |
| POST   | `/api/auth/register/`| Registers a new user                 |

---

## 🏡 Homepage API – Product Listing

This API serves **paginated**, **searchable**, and **filterable** product listings to be displayed on the homepage of the eCommerce application.

### 📍 Endpoint

| Method | Endpoint                 | Description                          |
|--------|--------------------------|--------------------------------------|
| GET    | `/products/homepage/`    | Returns a paginated product list for homepage |

### 🔍 Features

- ✅ Filtering by:
  - Category
  - In stock status
  - Active status
- 🔎 Searchable by:
  - Title
  - Company
- 📄 Pagination support:
  - `page` and `page_size` query params

### 🔧 Example Query

```
GET /products/homepage/?search=laptop&category=electronics&page=1&page_size=5
```

---

## 💻 Usage Example – Login (cURL)

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{"email": "admin@example.com", "password": "admin"}'
```

---

## 🛠 Environment Variables

Create a `.env` file in the root directory with:

```env
SECRET_KEY='django-insecure-fv_1_(d4v%8qdr_@r1ow+)a-@gq-+9j35^2067a$=gqohb^ozk'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## 🚀 Deployment

The API is live at:

```
http://127.0.0.1:8000
```

---

## 👩🏾‍💻 Contributors

- [Abigail Sylvester](https://github.com/sylvester-exp)

---

## 📝 License

This project is open-source under the [MIT License](https://opensource.org/licenses/MIT).
