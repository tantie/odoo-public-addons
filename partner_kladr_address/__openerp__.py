{
    'name': 'KLADR address',
    'version': '1.3',
    'category' : 'Sales Management',
    'summary': 'KLADR/FIAS addresses auto complete on a partner form',
    'author': 'IT Libertas',
    'website': 'http://itlibertas.com',
    'depends': ['base', 'web_kladr_widget'],
    'data': [
           'res_partner_view.xml',
           'res_bank_view.xml',
    ],
    'installable': True,
    'images': ['static/description/main.png'],
}
