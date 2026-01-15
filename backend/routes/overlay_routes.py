from flask import Blueprint, request, jsonify, current_app
from bson import ObjectId
from models.overlay_model import overlay_serializer

overlay_bp = Blueprint("overlay_bp", __name__)

# CREATE
@overlay_bp.route("/", methods=["POST"])
def create_overlay():
    data = request.json
    db = current_app.config["db"]
    
    overlay = {
        "x": data["x"],
        "y": data["y"],
        "width": data["width"],
        "height": data["height"],
        "content": data["content"],
        "type": data["type"]
    }

    result = db.overlays.insert_one(overlay)
    overlay["_id"] = result.inserted_id

    return jsonify(overlay_serializer(overlay)), 201


# READ ALL
@overlay_bp.route("/", methods=["GET"])
def get_overlays():
    db = current_app.config["db"]
    overlays = db.overlays.find()
    return jsonify([overlay_serializer(o) for o in overlays])


# UPDATE
@overlay_bp.route("/<id>", methods=["PUT"])
def update_overlay(id):
    data = request.json
    db = current_app.config["db"]

    db.overlays.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )

    overlay = db.overlays.find_one({"_id": ObjectId(id)})
    return jsonify(overlay_serializer(overlay))


# DELETE
@overlay_bp.route("/<id>", methods=["DELETE"])
def delete_overlay(id):
    db = current_app.config["db"]
    db.overlays.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Overlay deleted"})
