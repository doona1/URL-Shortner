from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)

# Configure Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define Database Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)

# Create Database Tables
with app.app_context():
    db.create_all()

# Function to Generate a Random Short Code
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None

    if request.method == "POST":
        long_url = request.form.get("long_url")
        if long_url:
            # Check if URL is already shortened
            existing_url = URL.query.filter_by(long_url=long_url).first()
            if existing_url:
                short_code = existing_url.short_code
            else:
                short_code = generate_short_code()
                new_url = URL(long_url=long_url, short_code=short_code)
                db.session.add(new_url)
                db.session.commit()

            short_url = f"http://127.0.0.1:5000/{short_code}"

    return render_template("index.html", short_url=short_url)

@app.route("/<short_code>")
def redirect_short_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        return redirect(url_entry.long_url)
    return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)
