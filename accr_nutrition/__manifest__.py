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
        'views/accr_food_type.xml',
        'views/accr_student_nutrition_details.xml',
        'views/accr_meal_type.xml',        
        'views/accr_meal_timing.xml',
        'views/accr_meal_timetable.xml',
        'views/accr_diet.xml',
        'views/accr_diet_plan.xml',
        'views/accr_nutrition_plan.xml',
        'views/accr_medical_contraindication.xml',
        'views/accr_student_view.xml',
        'views/accr_bca.xml',
        'views/accr_food.xml',
        'views/accr_student_orientation.xml',
        # 'wizard/accr_generate_meal_timetable_view.xml',
        'wizard/accr_generate_nutrition_students_view.xml',
        'reports/accr_student_nutrition_details.xml',
        'reports/accr_nutrition_student_report.xml',
        'menus/accr_nutrition_menu.xml',
    ],
}
