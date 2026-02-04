{
    'name' : 'Odoo School Library',
    'version' : '19.0.1.0.1',
    'author' : 'Odoo School',
    'website' : 'https://odoo.school',
    'category' : 'Customization',
    'license' : 'OPL-1',
    'depends' : ['base'],
    'external_dependencies' : {
        'python' : [],
    },
    'data' : [
        'security/ir.model.access.csv',
        'views/odoo_school_library_menu.xml',
        'views/odoo_school_library_book_views.xml'
    ],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'images': [
        'static/description/logo.png'
    ]
}
