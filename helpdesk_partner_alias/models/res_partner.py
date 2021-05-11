from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    helpdesk_alias = fields.Char(string='Name for tickets')
