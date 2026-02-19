"""
Professional Iris ML Web App
Author: Aishwarya Boda
Features:
- ML Prediction
- Beautiful UI
- SQLite Database
- Prediction History Page
"""

import sqlite3
import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load Model
model = pickle.load(open("model.pkl", "rb"))
species = ["Setosa", "Versicolor", "Virginica"]

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sepal_length REAL,
            sepal_width REAL,
            petal_length REAL,
            petal_width REAL,
            prediction TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        values = [float(x) for x in request.form.values()]
        final = np.array([values])

        pred = model.predict(final)[0]
        result = species[pred]

        # Save to DB
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO history VALUES (NULL,?,?,?,?,?)",
                  (*values, result))
        conn.commit()
        conn.close()

        return render_template("index.html",
                               prediction=result)

    except Exception as e:
        return render_template("index.html",
                               prediction=f"Error: {e}")

@app.route("/history")
def history():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history")
    rows = c.fetchall()
    conn.close()

    return render_template("history.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
