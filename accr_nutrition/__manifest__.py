{
    'name': 'ACCR Students Nutrition',
    'depends': ['base', 'mail', 'accr_medical_unit'],
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
        'views/accr_meal_timetable.xml',
        'views/accr_diet.xml',
        'views/accr_medical_contraindication.xml',
        'views/accr_student_view.xml',
        'wizard/accr_generate_meal_timetable_view.xml',
        'reports/accr_student_nutrition_details.xml',
        'menus/accr_nutrition_menu.xml',
    ],
}
