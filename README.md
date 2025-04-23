# 🛒 E-commerce Backend

A production-ready Django REST Framework backend for an e-commerce platform that connects customers with multiple retailers. Includes support for authentication, product listings, shopping carts, and more.

---

## 📖 Project Overview

This backend is built using Django and Django REST Framework to provide core API functionality for an e-commerce application. It supports:
- Token-based authentication (JWT)
- Product management with filtering, sorting, and search
- Customer shopping cart features
- API endpoints structured for frontend integration
- SQLite for development; production-ready setup

---

## ✨ Features

- JWT-based user authentication
- RESTful API endpoints
- Product creation, listing, and filtering
- Shopping cart with item add/remove/clear
- Admin panel integration for store managers
- Easily extendable product model with fields like `price`, `stock`, `subcategory`, `colour`, `usage`

---

## ⚙️ Installation

To get started with the backend locally:

```bash
# Clone the repo
git clone https://github.com/sylvester-exp/E-commerce-Backend
cd e-commerce-backend

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # on Windows use .venv\Scripts\activate

# Install dependencies
python3 -m pip install -r requirements.txt

# Run migrations
python3 manage.py migrate

# Create a superuser (optional for admin access)
python3 manage.py createsuperuser

# Start the server
python3 manage.py runserver

## API Endpoints

### Authentication Endpoints (`store/auth_urls.py`)
| Method | Endpoint              | Description                     |
|--------|-----------------------|---------------------------------|
| POST   | `/api/auth/login/`    | Login user and obtain JWT token. |
| POST   | `/api/auth/refresh/`  | Refresh JWT token.              |
| POST   | `/api/auth/register/` | Register a new user.            |

---

### Cart Endpoints (`cart/urls.py`)
| Method | Endpoint                     | Description                        |
|--------|------------------------------|------------------------------------|
| POST   | `/api/cart/add/`             | Add an item to the cart.           |
| DELETE | `/api/cart/remove/<item_id>/`| Remove an item from the cart.      |
| GET    | `/api/cart/items/`           | List all items in the cart.        |
| GET    | `/api/cart/detail/`          | Get cart details.                  |
| DELETE | `/api/cart/clear/`           | Clear all items from the cart.     |

---

### Homepage Endpoints (`homepage/urls.py`)
| Method | Endpoint                     | Description                        |
|--------|------------------------------|------------------------------------|
| GET    | `/`                          | View the homepage.                 |
| GET    | `/products/`                 | List all products.                 |
| GET    | `/products/homepage/`        | List homepage-specific products.   |
| GET    | `/products/home/`            | List home-specific products.       |

---

### Password Reset Endpoints (`urls.py`)
| Method | Endpoint                     | Description                        |
|--------|------------------------------|------------------------------------|
| GET    | `/password_reset/`           | Request a password reset.          |
| GET    | `/password_reset/done/`      | Password reset request confirmation.|
| GET    | `/reset/<uidb64>/<token>/`   | Confirm password reset token.      |
| GET    | `/reset/done/`               | Password reset completion page.    |

## Authentication

This project uses JWT (JSON Web Tokens) for secure authentication. Once a user logs in using /api/auth/login/, they receive an access and refresh token pair to interact with protected endpoints.

## Technologies Used

Python 3.13

Django 5.1.6

Django REST Framework 3.15.2

djangorestframework-simplejwt 5.x

SQLite (for dev)

pipenv / virtualenv

Created  by Abigail Sylvester