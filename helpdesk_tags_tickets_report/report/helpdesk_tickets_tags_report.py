# -*- coding: utf-8 -*-

from odoo import api, models


class HelpdeskTicketsTagsReport(models.AbstractModel):
    _name = "report.helpdesk_tags_tickets_report.helpdesk_ticket_template"

    @api.model
    def get_report_values(self, docids, data=None):

        return {
            "doc_ids": data["ticket_ids"],
            "doc_model": self.env["helpdesk.ticket"],
            "data": data,
            "docs": self.env["helpdesk.ticket"].browse(data["ticket_ids"]),
        }
