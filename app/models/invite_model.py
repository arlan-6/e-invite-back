from bson.objectid import ObjectId

class Invite:
    def __init__(self, mongo):
        self.collection = mongo.db.invites

    # Create invite
    def create_invite(self, invite_data):
        result = self.collection.insert_one(invite_data)
        return str(result.inserted_id)

    # Fetch all invites
    def get_invites(self):
        return list(self.collection.find())

    # Fetch single invite by ID
    def get_invite_by_id(self, invite_id):
        return self.collection.find_one({"_id": ObjectId(invite_id)})