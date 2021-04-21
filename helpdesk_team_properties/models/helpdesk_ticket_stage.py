from odoo import models, fields, api


class HelpdeskTicketStage(models.Model):
    _inherit = 'helpdesk.ticket.stage'

    team_id = fields.Many2one(
        comodel_name = 'helpdesk.ticket.team'
    )