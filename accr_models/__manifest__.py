# -*- coding: utf-8 -*-
{
    'name': "ACCR Models",

    'summary': """ACCR Models
       """,

    'description': """
        
    """,

    'author': "Mohamed Saber",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.12',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/weekly_plan.xml',
        'views/notes.xml',
        'views/monthly_plan.xml',
        'reports/notes_report.xml',
        'reports/weekly_report.xml',
        'reports/plan_report.xml',
        'reports/monthly_plan_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}