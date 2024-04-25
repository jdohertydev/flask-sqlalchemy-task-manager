import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# If there's an "env.py" file, import it
if os.path.exists("env.py"):
    import env  # noqa

# Create the Flask app
app = Flask(__name__)

# Set the secret key for Flask
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Set the database URI depending on the development environment
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after initializing Flask and SQLAlchemy
from taskmanager import routes  # noqa
