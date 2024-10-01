from app.models.invite_model import Invite


class InviteService:
    def __init__(self, mongo):
        # Store the mongo instance and pass it to the Invite model
        self.invite_model = Invite(mongo)

    def create_invite(self, invite_data):
        # Call the invite model to create a new invite
        return self.invite_model.create_invite(invite_data)

    def get_all_invites(self):
        # Call the invite model to retrieve all invites
        return self.invite_model.get_invites()
