# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Helpdesk Team Rules ',
    'summary': """
        Team specific tickets.
        """,

    'author': 'Calyx Servicios S.A., Odoo Community Association (OCA)',
    'maintainers': ['Github/Marcooegg'],

    'website': 'http://odoo.calyx-cloud.com.ar/',
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '11.0.2.0.0',
    # see https://odoo-community.org/page/development-status
    'development_status': 'Production/Stable',

    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },

    # any module necessary for this one to work correctly
    'depends': ['helpdesk_mgmt'],

    # always loaded
     'data': [
         'security/security.xml',
         'views/actions.xml',
     ],

}
