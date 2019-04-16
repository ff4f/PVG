{
    'name': 'ACCR Students Nutrition',
    'depends': ['base'],
    'application': True,
    'author': 'ACCR',

    'images': [
        'static/description/icon.png',
    ],

    'data': [
        'security/students_nutrition_security.xml',
        'security/ir.model.access.csv',
        'views/accr_student_nutrition_details.xml',
        'reports/accr_student_nutrition_details.xml ',
        'menus/accr_nutrition_menu.xml',
    ],
}
