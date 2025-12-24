from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# ---------------------------------------------------
# DATABASE CONFIG (Render + Neon)
# ---------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://neondb_owner:npg_FYH5UE6CBrwa@"
    "ep-morning-shape-a10y37q7-pooler.ap-southeast-1.aws.neon.tech/"
    "neondb?sslmode=require&channel_binding=require"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------------------------------------------------
# MODEL
# ---------------------------------------------------
class TestUser(db.Model):
    __tablename__ = "test_users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

# ---------------------------------------------------
# ROUTES
# ---------------------------------------------------
@app.route("/")
def home():
    return {"status": "Flask + Neon connected successfully 🚀"}

@app.route("/users")
def get_users():
    users = TestUser.query.all()
    return jsonify([
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ])

# ---------------------------------------------------
# LOCAL RUN ONLY
# ---------------------------------------------------
if __name__ == "__main__":
    app.run()
