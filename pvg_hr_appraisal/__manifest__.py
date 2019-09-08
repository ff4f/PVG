# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'PVG Appraisal',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 31,
    'summary': 'Extend for odoo hr appraisal',
    'depends': ['hr_appraisal'],
    'description': """
Extend for odoo hr appraisal
""",
    "data": [
        'views/hr_appraisal_views.xml',
        'reports/hr_appraisal_report.xml',
    ],
    'installable': True,
    'application': False,
}
