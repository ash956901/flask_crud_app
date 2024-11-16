from bson import ObjectId

def create_user(data, db):
    result = db.users.insert_one(data)
    return str(result.inserted_id)


def get_all_users(db):
    users = db.users.find()
    return [{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]


def get_user_by_id(user_id, db):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        return {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}
    return None


def update_user(user_id, data, db):
    result = db.users.find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": data},
        return_document=True
    )
    if result:
        return {"id": str(result["_id"]), "name": result["name"], "email": result["email"]}
    return None


def delete_user(user_id, db):
    result = db.users.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
