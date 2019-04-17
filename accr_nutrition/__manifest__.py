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
        'views/accr_food_group.xml',
        'views/accr_student_nutrition_details.xml',
        'views/accr_meal_type.xml',        
        'views/accr_meal_timing.xml',
        'reports/accr_student_nutrition_details.xml',
        'menus/accr_nutrition_menu.xml',
    ],
}
