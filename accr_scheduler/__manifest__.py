{
    'name': 'ACCR Students Scheduler',
    'depends': ['base'],
    'application': True,
    'author': 'ACCR',

    'images': [
        'static/description/icon.png',
    ],

    'data': [
        'security/students_scheduler_security.xml',
        'security/ir.model.access.csv',
        'views/accr_timing_view.xml',
        'views/accr_timetable_view.xml',
        'report/timetable_report_generate.xml'
        'report/report_menu.xml'
        'wizard/accr_generate_timetable_view.xml',
        'wizard/accr_time_table_report.xml',
        'menus/students_scheduler_menu.xml',
    ],
}
