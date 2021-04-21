from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    tag_ids = fields.Many2many(
        "helpdesk.ticket.tag", string="tag", help="tag")


'''
    @api.multi
    @api.onchange('team_id', 'user_id')
    def _onchange_dominion_user_id(self):
        super()._onchange_dominion_user_id()
        self.tag_id = False
'''