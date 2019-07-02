{
    'name': 'ACCR Students Resdiential',
    'depends': ['base', 'mail'],
    'application': True,
    'author': 'ACCR',

    'images': [
        'static/description/icon.png',
    ],

    'data': [
        'security/students_scheduler_security.xml',
        'security/ir.model.access.csv',
        'views/residential_nm_notification_view.xml',
    ],
}
