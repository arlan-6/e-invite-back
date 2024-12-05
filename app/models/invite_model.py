from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, make_response


class Test:
    def __init__(self, mongo):
        self.collection = mongo.db.templates

    def test(self):
        result = self.collection.find_one()
        if result and '_id' in result:
            result['_id'] = str(result['_id'])
        return result

class InviteEdits:
    def __init__(self, mongo):
        self.collection = mongo.db.userEditedTemplates

    # Create invite
    def create_invite(self, invite_data):
        if self.collection.find_one({"inviteId": invite_data.get("inviteId")}):
            raise ValueError("Duplicate inviteId found")
        # print(invite_data)
        self.collection.insert_one(invite_data)

        return invite_data.get("inviteId")

    # Fetch all invites
    def get_invites(self):
        return list(self.collection.find())

    # Fetch single invite by ID
    def get_invite_by_id(self, invite_id):
        invite = self.collection.find_one({"inviteId": invite_id})

        if invite and '_id' in invite:
            invite['_id'] = str(invite['_id'])
        return invite

    # Fetch invites by email
    def get_invites_by_email(self, email):
        invites = list(self.collection.find({"email": email}))
        for invite in invites:
            if '_id' in invite:
                invite['_id'] = str(invite['_id'])
        return invites

    # Update invite by ID
    def update_invite(self, invite_id, invite_data):
        if '_id' in invite_data:
            del invite_data['_id']
        self.collection.update_one(
            {"inviteId": invite_id},
            {"$set": invite_data}
        )
        return self.get_invite_by_id(invite_id)

    # Delete invite by ID
    def delete_invite(self, invite_id):
        self.collection.delete_one({"id":invite_id})

    # Fetch invites by user email
    def get_invites_by_user(self, user_email):
        return list(self.collection.find({"email": user_email}))


# Template class to handle templates
class Template:
    def __init__(self, mongo):
        self.collection = mongo.db.templates
        self.liked = mongo.db.likedTemplate

    # Fetch all templates
    def get_templates(self):
        templates = list(self.collection.find())
        for template in templates:
            template['_id'] = str(template['_id'])
        # print(templates)
        return templates

    def get_template_by_id(self, template_id):
        template = self.collection.find_one({"id": template_id})
        if template and '_id' in template:
            template['_id'] = str(template['_id'])
        return template

    def post_template(self, template_data):
        result = self.collection.insert_one(template_data)
        return str(result.inserted_id)

    def like_template(self, user_email, template_id):
        # Find the user by email
        user = self.liked.find_one({"email": user_email})

        if user:
            # Add the template_id to the likedTemplateId list if it's not already there
            if template_id not in user['likedTemplateId']:
                self.liked.update_one(
                    {"email": user_email},
                    {"$push": {"likedTemplateId": template_id}}
                )
        else:
            # If the user does not exist, create a new document
            self.liked.insert_one({
                "email": user_email,
                "likedTemplateId": [template_id]
            })

    def get_liked_templates(self, user_email):
        user = self.liked.find_one({"email": user_email})
        if user:
            return user['likedTemplateId']
        return []


    def unlike_template(self, user_email, template_id):
        user = self.liked.find_one({"email": user_email})
        if user:
            self.liked.update_one(
                {"email": user_email},
                {"$pull": {"likedTemplateId": template_id}}
            )


class Invites:
    def __init__(self, mongo):
        self.collection = mongo.db.invites

    def publish_invite(self, invite_data):
        # existing_invite = self.collection.find_one({"inviteId": invite_data.get("inviteId")})
        # if existing_invite:
        #     print('duplicate inviteId found')
        #     return {"error": "Duplicate inviteId found", "id": existing_invite.get("id")}, 400
            # return {"error": "Duplicate inviteId found", "id": existing_invite.get("id")}, 500
        self.collection.insert_one(invite_data)
        return {"id": invite_data.get("id")}, 201

    def is_duplicate(self, invite_data):
        return self.collection.find_one({"inviteId": invite_data.get("inviteId")})

    def get_invites(self):
        return list(self.collection.find())

    def get_invite_by_id(self, invite_id):
        invite = self.collection.find_one({"id": invite_id})
        if invite and '_id' in invite:
            invite['_id'] = str(invite['_id'])
        return invite

    def get_invites_by_email(self, email):
        invites = list(self.collection.find({"email": email}))
        for invite in invites:
            if '_id' in invite:
                invite['_id'] = str(invite['_id'])
        return invites

    def update_rsvp(self, invite_id, rsvp_data):
        self.collection.update_one(
            {"id": invite_id},
            {"$push": {"rsvp": rsvp_data}}
        )
        return self.get_invite_by_id(invite_id)

    def update_invite(self, invite_id, invite_data):
        if '_id' in invite_data:
            del invite_data['_id']
        self.collection.update_one(
            {"id": invite_id},
            {"$set": invite_data}
        )
        return self.get_invite_by_id(invite_id)

    def update_invite_remove_rsvp(self, invite_id, invite_data):
        self.collection.update_one(
            {"id": invite_id},
            {"$pull": {"rsvp": invite_data}}
        )
        return self.get_invite_by_id(invite_id)

    def delete_invite(self, invite_id):
        self.collection.delete_one({"id": invite_id})

    def get_invites_by_user(self, user_email):
        return list(self.collection.find({"email": user_email}))