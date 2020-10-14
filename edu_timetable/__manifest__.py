# -*- coding: utf-8 -*-
###############################################################################
#
#
###############################################################################
{
    'name': 'EDU Timetable',
    'version': '13.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage TimeTables',
    'complexity': "easy",
    'depends': ['mail','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/sequence.xml',
        'views/timetable_view.xml',
        'views/timing_view.xml',
    ],
    'demo': [
    ],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
