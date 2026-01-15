from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__, static_folder="static")
CORS(app)

DB_FILE = "overlays.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS overlays (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            x INTEGER,
            y INTEGER,
            width INTEGER,
            height INTEGER,
            content TEXT,
            type TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------- CRUD APIs ---------------- #

@app.route("/api/overlays/", methods=["GET"])
def get_overlays():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM overlays")
    rows = c.fetchall()
    conn.close()

    overlays = []
    for row in rows:
        overlays.append({
            "id": row[0],
            "x": row[1],
            "y": row[2],
            "width": row[3],
            "height": row[4],
            "content": row[5],
            "type": row[6]
        })

    return jsonify(overlays)


@app.route("/api/overlays/", methods=["POST"])
def create_overlay():
    data = request.json
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("""
        INSERT INTO overlays (x, y, width, height, content, type)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data["x"], data["y"], data["width"], data["height"], data["content"], data["type"]))

    conn.commit()
    conn.close()

    return jsonify({"message": "Overlay created"}), 201


@app.route("/api/overlays/<int:id>", methods=["PUT"])
def update_overlay(id):
    data = request.json
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("SELECT * FROM overlays WHERE id=?", (id,))
    row = c.fetchone()

    if not row:
        conn.close()
        return jsonify({"error": "Overlay not found"}), 404

    updated = {
        "x": data.get("x", row[1]),
        "y": data.get("y", row[2]),
        "width": data.get("width", row[3]),
        "height": data.get("height", row[4]),
        "content": data.get("content", row[5]),
        "type": data.get("type", row[6])
    }

    c.execute("""
        UPDATE overlays
        SET x=?, y=?, width=?, height=?, content=?, type=?
        WHERE id=?
    """, (
        updated["x"],
        updated["y"],
        updated["width"],
        updated["height"],
        updated["content"],
        updated["type"],
        id
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Overlay updated"})

@app.route("/api/overlays/<int:id>", methods=["DELETE"])
def delete_overlay(id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM overlays WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Overlay deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
