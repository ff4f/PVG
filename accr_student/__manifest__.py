{
    'name': 'ACCR Students',
    'depends': ['base', 'mail'],
    'application': True,
    'author': 'ACCR',

    'images': [
        'static/description/icon.png',
    ],

    'data': [
        'security/accr_students_security.xml',
        'security/ir.model.access.csv',
        'views/accr_students_notifications_view.xml',
        'menus/accr_students_menu.xml',
    ],
}
