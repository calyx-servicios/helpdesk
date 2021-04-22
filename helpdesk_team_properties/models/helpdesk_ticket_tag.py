from odoo import models, fields, api


class HelpdeskTicketTag(models.Model):
    _inherit = 'helpdesk.ticket.tag'

    team_id = fields.Many2one(
        comodel_name = 'helpdesk.ticket.team'
    )