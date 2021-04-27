from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    ticket_team_id = fields.Many2many('helpdesk.ticket.team', string='Ticket teams')