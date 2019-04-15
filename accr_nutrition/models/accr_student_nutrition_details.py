from odoo import models, fields, api

class accrStudentNutritionDetails(models.Model):
    _name = "accr.student.nutrition.details"
    _description = "Student Nutrition Details"
    
    student = fields.Many2one(
        string=u'Student',
        comodel_name='model.x_student',
        ondelete='set restrict',
    )
    name = fields.Char('Name', related='student.x_name',)
    age = fields.Integer('Age', related='student.x_studio_age',)
    diagnosis = fields.Char('Diagnosis', related='student.x_studio_diagnosis',)
    residential_section = fields.Char('Residential Section', related='student.x_studio_residential_section',)
    medications = fields.One2many('Medications', related='student.x_studio_field_jm5yW',)
    food_preferences = fields.One2many('accr.food.preferences', 'student_nutrition_details', 'Food Preferences',)

    height = fields.Integer('Height', required=True,)
    weight = fields.Integer('Weight', required=True,)
    diet = fields.Char('Diet',)
    requirements = fields.Char('Requirements',)
    physical_activity = fields.Char('Physical Activity',)
    water_intake = fields.Char('Water Intake',)



    