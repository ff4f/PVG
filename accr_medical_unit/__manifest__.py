{
    'name': 'ACCR Medical Unit',
    'depends': ['base', 'mail', 'web_studio'],
    'application': True,
    'author': 'ACCR',

    'images': [
        'static/description/icon.png',
    ],

    'data': [
        'security/accr_medical_unit_security.xml',
        'security/ir.model.access.csv',
        'views/accr_medical_unit_medicine_side_effects_view.xml',
        'views/accr_medical_unit_medicine_view.xml',
        'views/accr_medical_unit_medication_view.xml',
        'menus/accr_medical_unit_menu.xml',
    ],
}
