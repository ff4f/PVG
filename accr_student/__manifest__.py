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
        'views/accr_student_se_report_view.xml',
        'reports/accr_student_se_report.xml',
        'reports/accr_student_se_report_ar.xml',
        'reports/accr_student_se_report_ar_2.xml',
        'menus/accr_students_menu.xml',
    ],
}
