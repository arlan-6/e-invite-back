from app.models.invite_model import InviteEdits, Template, Invites,Test

class TestService:
    def __init__(self, mongo):
        self.test_model = Test(mongo)

    def test(self):
        return self.test_model.test()

class InviteTemplateService:
    def __init__(self, mongo):
        # Store the mongo instance and pass it to the Invite model
        self.invite_edit_model = InviteEdits(mongo)
        self.template_model = Template(mongo)

    def create_invite(self, invite_data):
        # Call the invite model to create a new invite
        return self.invite_edit_model.create_invite(invite_data)

    def get_all_invites(self):
        # Call the invite model to retrieve all invites
        return self.invite_edit_model.get_invites()

    def get_invite_by_id(self, invite_id):
        # Call the invite model to retrieve an invite by ID
        return self.invite_edit_model.get_invite_by_id(invite_id)

    def update_invite(self, invite_id, invite_data):
        # Call the invite model to update an invite by ID
        return self.invite_edit_model.update_invite(invite_id, invite_data)

    def delete_invite(self, invite_id):
        # Call the invite model to delete an invite by ID
        return self.invite_edit_model.delete_invite(invite_id)

    def get_invites_by_email(self, email):
        # Call the invite model to retrieve invites by email
        return self.invite_edit_model.get_invites_by_email(email)

    def get_all_templates(self):
        # Call the invite model to retrieve all templates
        return self.template_model.get_templates()

    def get_template_by_id(self, template_id):
        # Call the template model to retrieve a template by ID
        return self.template_model.get_template_by_id(template_id)

    def create_template(self, template_data):
        # Call the template model to create a new template
        return self.template_model.post_template(template_data)

    def like_template(self, user_email, template_id):
        # Call the template model to like a template
        return self.template_model.like_template(user_email, template_id)

    def get_liked_templates(self, user_email):
        # Call the template model to get liked templates
        return self.template_model.get_liked_templates(user_email)

    def unlike_template(self, user_email, template_id):
        # Call the template model to unlike a template
        return self.template_model.unlike_template(user_email, template_id)

    # ------------------- Invite Service -------------------

class InviteService:
    def __init__(self, mongo):
        self.invite_model = Invites(mongo)

    def publish_invite(self, invite_data):
        return self.invite_model.publish_invite(invite_data)

    def is_duplicate(self, invite_data):
        return self.invite_model.is_duplicate(invite_data)

    # def create_invite(self, invite_data):
    #     return self.invite_model.create_invite(invite_data)
    #
    def get_invite_by_id(self, invite_id):
        return self.invite_model.get_invite_by_id(invite_id)

    def get_users_invites_by_email(self, email):
        return self.invite_model.get_invites_by_email(email)


    # def get_invites_by_email(self, email):
    #     return self.invite_model.get_invites_by_email(email)
    #
    def update_invite(self, invite_id, invite_data):
        return self.invite_model.update_rsvp(invite_id, invite_data)

    def update_invite_remove_rsvp(self, invite_id, invite_data):
        return self.invite_model.update_invite_remove_rsvp(invite_id, invite_data)

    def delete_invite(self, invite_id):
        return self.invite_model.delete_invite(invite_id)

