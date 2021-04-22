from odoo import models, fields, api


class HelpdeskTicketTeam(models.Model):
    _inherit = 'helpdesk.ticket.team'

    tag_ids = fields.One2many(
        'helpdesk.ticket.tag',
        'team_id',
        string = 'Tags'
    )
    category_ids = fields.One2many(
        'helpdesk.ticket.category',
        'team_id',
        string = 'Categories'
    )
    stage_ids = fields.One2many(
        'helpdesk.ticket.stage',
        'team_id',
        string = 'Stages'
    )
    motive_ids = fields.One2many(
        'helpdesk.ticket.motive',
        'team_id',
        string = 'Motives'
    )
    '''
    '''