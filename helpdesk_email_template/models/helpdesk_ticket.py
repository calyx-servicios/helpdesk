from odoo import _, api, fields, models, tools


class HelpdeskTicket(models.Model):

    _inherit = 'helpdesk.ticket'

    @api.multi
    def get_full_url(self):
        self.ensure_one()
        base_url = self.env["ir.config_parameter"].get_param("web.base.url")
        return base_url + '/web#' + 'id=' + str(self.id) + '&view_type=form&model=helpdesk.ticket&active_id=1' 

    def send_user_mail(self):
        self.env.ref('helpdesk_email_template.assignment_email_template'). \
            send_mail(self.id)