{
    'name': 'Helpdesk mail template',
    'author': 'Calyx Servicios S.A., Odoo Community Association (OCA)',
    'maintainers': ['Cristian Paradiso'],
    'website': 'http://odoo.calyx-cloud.com.ar/',
    'license': 'AGPL-3',
    'category': 'Technical Settings',
    'version': '11.0.1.0.0',
    'development_status': 'Production/Stable',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
 
    'depends': ['helpdesk_mgmt'],

    'data': [
         'data/helpdesk_data.xml',
    ],

}
