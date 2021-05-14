from odoo import models, fields, api


class AccountMoveFYReport(models.TransientModel):
    _name = "helpdesk.ticket.tags.wizard"

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To", default=fields.Date.context_today)
    team_id = fields.Many2one(
        "helpdesk.ticket.team", string="Helpdesk Team", required=True, index=True
    )
    user_id = fields.Many2one("res.users", string="Assigned User")
    partner_id = fields.Many2one("res.partner", string="Company")
    category_id = fields.Many2one("helpdesk.ticket.category", string="Category")
    motive_id = fields.Many2one("helpdesk.ticket.motive", string="Motive")
    tag_id = fields.Many2many("helpdesk.ticket.tag", string="Tag", required=True)

    @api.multi
    def print_report(self):
        # ################
        # Tickets Query
        # ################

        query = [
            ("team_id", "=", self.team_id.id),
            ("tag_ids", "in", self.tag_id.ids),
            ("company_id", "=", self.env.user.company_id.id),
        ]

        if self.date_from:
            query.append(("create_date", ">=", self.date_from))
        if self.date_to:
            query.append(("create_date", "<=", self.date_to))
        if self.user_id:
            query.append(("user_id", "=", self.user_id.id))
        if self.partner_id:
            query.append(("partner_id", "=", self.partner_id.id))
        if self.category_id:
            query.append(("category_id", "=", self.category_id.id))
        if self.motive_id:
            query.append(("motive_id", "=", self.motive_id.id))

        ticket_objs = self.env["helpdesk.ticket"].search(query, order="create_date asc")

        # ##########################
        # Data Form
        # ##########################
        data = {
            "date_from": self.date_from,
            "date_to": self.date_to,
        }

        datas = {"ticket_ids": ticket_objs.ids, "form": data}

        # ############
        # CALL REPORT
        # ############
        return self.env.ref(
            "helpdesk_tags_tickets_report.action_tickets_report"
        ).report_action(self, data=datas)
