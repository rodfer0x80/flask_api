from flask import Blueprint, jsonify

from .app import app

@app.route("/", methods=["GET", "POST"])
def index():
    data = {
            "type":[
                {"name": "name_zero", "id": 0},
                {"name": "name_one", "id": 1},
                {"name": "name_two", "id": 2},
                ]
        }
    return jsonify(data)
