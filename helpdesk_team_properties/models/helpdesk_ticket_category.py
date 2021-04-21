from odoo import models, fields, api


class HelpdeskTicketCategory(models.Model):
    _inherit = 'helpdesk.ticket.category'

    team_id = fields.Many2one(
        comodel_name = 'helpdesk.ticket.team'
    )