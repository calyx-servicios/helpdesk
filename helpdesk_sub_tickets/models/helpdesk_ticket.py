from odoo import fields, models, api
from odoo.exceptions import ValidationError

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    parent_id = fields.Many2one(
        'helpdesk.ticket',
        string = 'Parent Ticket',
        ondelete='restrict',
        index = True
    )
    child_ids = fields.One2many(
        'helpdesk.ticket',
        'parent_id',
        string = 'Child Tickets'
    )

    #prevents recursive relationships
    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError(
                'Error! You cannot create recursive tickets'
            )
    