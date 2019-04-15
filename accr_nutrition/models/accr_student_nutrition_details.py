from odoo import models, fields, api, _

class accrStudentNutritionDetails(models.Model):
    _name = "accr.student.nutrition.details"
    _description = "Student Nutrition Details"
    
    student = fields.Many2one('x_student', 'Student', required=True, ondelete='set restrict', )
    name = fields.Char(related='student.display_name', string='Name', readonly=True, )
    age = fields.Integer(related='student.x_studio_age', string="Age", readonly=True, )
    diagnosis = fields.Text(related='student.x_studio_diagnosis', string='Diagnosis', readonly=True, )
    residential_section = fields.Many2one(related='student.x_studio_residential_sections', string='Residential Section', readonly=True, )
    medications = fields.One2many(related='student.x_studio_field_jm5yW', string='Medications', readonly=True, )
    food_preferences = fields.One2many('accr.food.preferences', 'student_nutrition_details', 'Food Preferences', )

    height = fields.Integer('Height', required=True, )
    weight = fields.Integer('Weight', required=True, )
    diet = fields.Char('Diet', )
    requirements = fields.Char('Requirements', )
    physical_activity = fields.Char('Physical Activity', )
    water_intake = fields.Char('Water Intake', )