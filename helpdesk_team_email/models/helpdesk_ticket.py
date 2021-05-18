from odoo import _, api, fields, models, tools


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    def send_team_email(self):
        self.env.ref("helpdesk_team_email.team_assignment_email_template").send_mail(
            self.id
        )

    @api.model
    def get_email_to_team(self):
        email_list = [
            usr.partner_id.email
            for usr in self.team_id.user_ids
            if usr.partner_id.email
        ]
        return ",".join(email_list)

    # ---------------------------------------------------
    # CRUD
    # ---------------------------------------------------

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if vals.get("team_id") and res:
            res.send_team_email()
            if not vals.get("assigned_date"):
                res["assigned_date"] = fields.Datetime.now()
        return res

    @api.multi
    def write(self, vals):
        res = super(HelpdeskTicket, self).write(vals)
        for ticket in self:
            if vals.get("team_id"):
                ticket.send_team_email()
        return res