from flask import Blueprint, request, jsonify
from bson import ObjectId
from app.mongo import mongo
from app.models import UserSchema
from app.utils import hash_password, verify_password

api = Blueprint("api", __name__)
user_schema = UserSchema()

@api.route("/", methods=["GET"])
def index():
    
    return jsonify({"message": "Hello, World!"}), 200

@api.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    result = [{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]
    return jsonify(result), 200

@api.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if not user:
        return jsonify({"error": "User not found"}), 404
    result = {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}
    return jsonify(result), 200

@api.route("/users", methods=["POST"])
def create_user():
    data = request.json
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    data["password"] = hash_password(data["password"])
    inserted_id = mongo.db.users.insert_one(data).inserted_id
    return jsonify({"id": str(inserted_id)}), 201

@api.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.json
    if "password" in data:
        data["password"] = hash_password(data["password"])
    result = mongo.db.users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": data}, return_document=True
    )
    if not result:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User updated successfully"}), 200

@api.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = mongo.db.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200
