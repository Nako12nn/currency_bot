# Currency Tracker Bot

Telegram bot + REST API for tracking currency rates with caching, async backend, and Dockerized infrastructure.

##  Features

* Telegram bot (Aiogram)
*  FastAPI REST API
*  PostgreSQL (async SQLAlchemy)
*  Redis caching
*  JWT authentication (API)
*  Docker & Docker Compose
*  Pytest (unit & async tests)
*  CI (GitHub Actions)
*  Environment-based configuration (`.env`)

---

##  Tech Stack

**Backend**

* Python 3.11+
* FastAPI
* Aiogram
* Async SQLAlchemy
* Pydantic v2

**Databases & Cache**

* PostgreSQL
* Redis

**DevOps**

* Docker / Docker Compose
* GitHub Actions (CI)

**Testing**

* Pytest
* pytest-asyncio
* monkeypatch

---

## Project Structure

```
currency_bot/
│
├── app/
│   ├── api/                # FastAPI routes
│   ├── bot/                # Telegram bot logic
│   ├── config.py           # App settings (Pydantic)
│   ├── database/           # DB models & CRUD
│   ├── services/           # Redis, business logic
│   └── main.py             # App entrypoint
│
├── tests/                  # Unit & async tests
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql+asyncpg://currency_user:currency_pass@db:5432/currency_db
REDIS_URL=redis://redis:6379
TELEGRAM_TOKEN=your_telegram_bot_token
SECRET_KEY=super_secret_key
```

---

## 🐳 Run with Docker

```bash
docker compose up --build
```

Services:

* FastAPI → [http://localhost:8000](http://localhost:8000)
* Swagger → [http://localhost:8000/docs](http://localhost:8000/docs)
* PostgreSQL → port 5432
* Redis → port 6379

---

## 📡 API Endpoints

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| GET    | /currencies | List currencies |
| GET    | /rates      | Currency rates  |
| POST   | /auth/login | JWT login       |
| GET    | /docs       | Swagger UI      |

---

##  Telegram Bot

* Gets currency rates
* Uses Redis caching
* Async polling
* Works inside Docker

---

##  Run Tests

```bash
pytest
```

Tests include:

* business logic
* Redis cache (mocked)
* async database access

---

##  CI (GitHub Actions)

On every push:

* installs dependencies
* runs tests
* validates codebase

---

##  Author

**Maksym**
Python Developer

---

##  Notes for Reviewers

If Docker build fails due to cache issues, run:

```bash
docker builder prune -af
```
