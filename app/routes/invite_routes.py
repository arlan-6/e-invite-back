from flask import Blueprint, request, jsonify
from app.services.invite_service import InviteService, InviteTemplateService
from app.app import mongo

invite_bp = Blueprint('invite_bp', __name__)
invite_template_service = InviteTemplateService(mongo)
invite_service = InviteService(mongo)

@invite_bp.route('/test', methods=['GET'])
def test_mongo_connection():
    try:
        mongo.db.command('ping')
        return jsonify({"message": "MongoDB connection is successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@invite_bp.route('/edit/invites', methods=['GET'])
def get_invites():
    invites = invite_template_service.get_all_invites()
    return jsonify(invites), 200

@invite_bp.route('/edit/invites', methods=['POST'])
def create_invite():
    invite_data = request.json
    # print(f"Received invite data: {invite_data}")
    invite_id = invite_template_service.create_invite(invite_data)
    # print(f"Generated invite ID: {invite_id}")
    return jsonify({"id": invite_id}), 201

@invite_bp.route('/edit/invites/<invite_id>', methods=['GET'])
def get_invite_by_id(invite_id):
    invite = invite_template_service.get_invite_by_id(invite_id)
    return jsonify(invite), 200

@invite_bp.route('/edit/invites/email', methods=['GET'])
def get_invites_by_email():
    email = request.args.get('email')
    invites = invite_template_service.get_invites_by_email(email)
    return jsonify(invites), 200

@invite_bp.route('/edit/invites/<invite_id>', methods=['PUT'])
def update_invite(invite_id):
    invite_data = request.json
    updated_invite = invite_template_service.update_invite(invite_id, invite_data)
    return jsonify(updated_invite), 200

@invite_bp.route('/edit/invites/<invite_id>', methods=['DELETE'])
def delete_invite(invite_id):
    invite_template_service.delete_invite(invite_id)
    return jsonify({"message": "Invite deleted"}), 200

@invite_bp.route('/templates', methods=['GET'])
def get_templates():
    templates = invite_template_service.get_all_templates()
    return jsonify(templates), 200

@invite_bp.route('/templates/<template_id>', methods=['GET'])
def get_template_by_id(template_id):
    template = invite_template_service.get_template_by_id(template_id)
    return jsonify(template), 200

@invite_bp.route('/templates', methods=['POST'])
def create_template():
    template_data = request.json
    template_id = invite_template_service.create_template(template_data)
    return jsonify({"id": template_id}), 201

@invite_bp.route('/templates/like', methods=['POST'])
def like_template():
    data = request.json
    user_email = data.get('email')
    template_id = data.get('templateId')
    invite_template_service.like_template(user_email, template_id)
    return jsonify({"message": "Template liked"}), 200

@invite_bp.route('/templates/liked', methods=['GET'])
def get_liked_templates():
    user_email = request.args.get('email')
    templates = invite_template_service.get_liked_templates(user_email)
    # print(templates)
    return jsonify(templates), 200

@invite_bp.route('/templates/unlike', methods=['POST'])
def unlike_template():
    data = request.json
    user_email = data.get('email')
    template_id = data.get('templateId')
    invite_template_service.unlike_template(user_email, template_id)
    return jsonify({"message": "Template unliked"}), 200

# ------------------- Invite Blueprint -------------------

@invite_bp.route('/invites/publish', methods=['POST'])
def publish_invite():
    invite_data = request.json
    if invite_service.is_duplicate(invite_data):
        return jsonify({"error": "Duplicate invite found","id":invite_service.is_duplicate(invite_data).get("id")}), 400
    invite_id = invite_service.publish_invite(invite_data)
    return jsonify({"id": invite_id}), 201

@invite_bp.route('/invites/published/<invite_id>', methods=['GET'])
def get_published_invite(invite_id):
    invite = invite_service.get_invite_by_id(invite_id)
    return jsonify(invite), 200

@invite_bp.route('/invites', methods=['GET'])
def get_users_invites_by_email():
    email = request.args.get('email')
    invites = invite_service.get_users_invites_by_email(email)
    return jsonify(invites), 200

@invite_bp.route('/invites/delete/<invite_id>', methods=['DELETE'])
def delete_invite_by_id(invite_id):
    invite_service.delete_invite(invite_id)
    return jsonify({"message": "Invite deleted"}), 200

@invite_bp.route('/invites/update/<invite_id>', methods=['PUT'])
def update_invite_by_id(invite_id):
    invite_data = request.json
    updated_invite = invite_service.update_invite(invite_id, invite_data)
    return jsonify(updated_invite), 200

@invite_bp.route('/invites/delete/rsvp/<invite_id>', methods=['PUT'])
def delete_rsvp(invite_id):
    invite_data = request.json
    updated_invite = invite_service.update_invite_remove_rsvp(invite_id, invite_data)
    return jsonify(updated_invite), 200