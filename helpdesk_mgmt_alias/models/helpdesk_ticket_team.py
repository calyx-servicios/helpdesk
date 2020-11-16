from odoo import models, api, fields
from odoo.tools.safe_eval import safe_eval


class HelpdeskTeam(models.Model):

    _name = "helpdesk.ticket.team"
    _inherit = ["helpdesk.ticket.team", "mail.thread", "mail.alias.mixin"]

    alias_id = fields.Many2one(
        comodel_name="mail.alias",
        string="Email",
        ondelete="restrict",
        required=True,
        help="The email address associated with \
                                this channel. New emails received will \
                                automatically create new tickets assigned \
                                to the channel.",
    )

    def get_alias_model_name(self, vals):
        return "helpdesk.ticket"

    def get_alias_values(self):
        values = super().get_alias_values()
        values["alias_defaults"] = defaults = safe_eval(self.alias_defaults or "{}")
        defaults["team_id"] = self.id
        return values
