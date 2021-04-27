from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    #@api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['helpdesk.ticket.stage'].search([('team_id','in',self.user_id.team_id)])
        return stage_ids