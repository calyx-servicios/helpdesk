# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Tags Tickets Report",
    "summary": """
        This module adds a wizard to print Tickets Reports by tags.""",
    "author": "Calyx Servicios S.A., Odoo Community Association (OCA)",
    "maintainers": ["FedericoGregori"],
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Helpdesk",
    "version": "11.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    # any module necessary for this one to work correctly
    "depends": ["helpdesk_mgmt", "helpdesk_motive"],
    # always loaded
    "data": [
        "wizard/helpdesk_ticket_tags_wizard.xml",
        "report/helpdesk_tickets_tags_report.xml",
    ],
}
