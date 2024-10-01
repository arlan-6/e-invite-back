from flask import Blueprint, request, jsonify
from app.services.invite_service import InviteService
from app.app import mongo

invite_bp = Blueprint('invite_bp', __name__)
invite_service = InviteService(mongo)

@invite_bp.route('/invites', methods=['GET'])
def get_invites():
    invites = invite_service.get_all_invites()
    return jsonify(invites), 200

@invite_bp.route('/invites', methods=['POST'])
def create_invite():
    invite_data = request.json
    invite_id = invite_service.create_invite(invite_data)
    return jsonify({"id": invite_id}), 201