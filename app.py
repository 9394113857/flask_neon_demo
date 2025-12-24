from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ---------------------------------------------------
# DIRECT NEON DATABASE CONNECTION (LOCAL TEST ONLY)
# ---------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg://neondb_owner:npg_FYH5UE6CBrwa@"
    "ep-morning-shape-a10y37q7-pooler.ap-southeast-1.aws.neon.tech/"
    "neondb?sslmode=require&channel_binding=require"
)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------------------------------------------------
# MODEL (maps to existing table)
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

@app.route("/users", methods=["GET"])
def get_users():
    users = TestUser.query.all()

    data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        for user in users
    ]

    return jsonify(data)

# ---------------------------------------------------
# RUN
# ---------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
