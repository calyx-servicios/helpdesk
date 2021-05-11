from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    partner_alias = fields.Char('Partner Name',
        related = 'partner_id.helpdesk_alias', 
        readonly = True
    )
