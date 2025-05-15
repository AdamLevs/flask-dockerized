# Flaskr — Production-Ready Flask App

![Flask plus Codefresh](docker-flask-codefresh.jpg)


This is a Dockerized, production-ready version of the official [Flask tutorial app](https://github.com/pallets/flask/tree/main/examples/tutorial).  
It includes best practices for running Flask in production using:

- ⚙️ Flask (modular app structure)
- 🐘 PostgreSQL database
- 🔥 Gunicorn WSGI server
- 🌐 Nginx as a reverse proxy
- 🐳 Docker & Docker Compose

---

## 🧰 Features

- User authentication (register/login/logout)
- Blog post creation, editing, and deletion
- Database migrations and init via CLI
- Static files & templates separation
- Clean separation between dev and production
- Custom CSS styling with light, modern design

---

## 🚀 Quick Start

Clone the project and run it using Docker Compose:

```bash
git clone https://github.com/your-user/flaskr-app.git
cd flaskr-app
docker compose up --build
``` 

## 🧱 Project Structure
```
.
├── flaskr/             # Core app: auth, blog, db, schema.sql
│   ├── templates/      # Jinja2 templates
│   └── static/         # CSS and other assets
├── instance/           # SQLite DB or instance files
├── static/             # Public static (linked via Nginx)
├── wsgi.py             # Gunicorn entrypoint
├── Dockerfile          # Flask + Gunicorn image
├── nginx.conf          # Nginx proxy config
├── docker-compose.yaml
└── requirements.txt
```
## ⚙️ Environment Variables
```bash
FLASK_APP=flaskr
FLASK_ENV=production
DATABASE_URL=postgresql://flaskr:flaskr@db:5432/flaskr
```
## 🧪 Running Locally (Without Docker)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
export FLASK_APP=flaskr
flask init-db
flask run --host=0.0.0.0
```
    