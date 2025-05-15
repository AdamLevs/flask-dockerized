import os
import click
import psycopg2
import psycopg2.extras
from urllib.parse import urlparse
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


def get_db():
    if "db" not in g:
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise RuntimeError("DATABASE_URL is not set")

        result = urlparse(db_url)

        g.db = psycopg2.connect(
            dbname=result.path[1:],
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port,
            cursor_factory=psycopg2.extras.RealDictCursor  # 🧠 מחזיר dict לכל שורה
        )

    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    cursor = db.cursor()
    with current_app.open_resource("schema.sql") as f:
        cursor.execute(f.read().decode("utf8"))
    db.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def create_demo_user():
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            'INSERT INTO "user" (username, password) VALUES (%s, %s)',
            ("admin", generate_password_hash("admin"))
        )
        db.commit()
        print("▶ Demo user 'admin' created with password 'admin'")
    except psycopg2.errors.UniqueViolation:
        db.rollback()
        print("▶ Demo user already exists. Skipping.")


@click.command("init-demo")
@with_appcontext
def init_demo_command():
    """Create a demo user if not exists."""
    create_demo_user()
    click.echo("Created demo user.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(init_demo_command)
