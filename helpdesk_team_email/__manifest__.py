# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Team Email",
    "summary": """
        With this module, any time a Ticket is created o edited, a mail will be sent to every member of the assigned team""",
    "author": "Calyx Servicios S.A., Odoo Community Association (OCA)",
    "maintainers": ["FedericoGregori"],
    "website": "http://odoo.calyx-cloud.com.ar/",
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
    "depends": ["base", "helpdesk_mgmt"],
    # always loaded
    "data": [
        "data/helpdesk_data.xml",
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
