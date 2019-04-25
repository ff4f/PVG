{
    'name': 'ACCR Medical_unit',
    'depends': ['base', 'mail'],
    'application': True,
    'author': 'ACCR',

    'images': [
        'static/description/icon.png',
    ],

    'data': [
        'security/accr_medical_unit_security.xml',
        'security/ir.model.access.csv',
        'views/accr_medical_unit_medication_side_effects_view.xml',
        'views/accr_medical_unit_medication_view.xml',
        'menus/accr_medical_unit_menu.xml',
    ],
}
