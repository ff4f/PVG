from odoo import models, fields, api, _

class accrStudentNutritionDetails(models.Model):
    _name = "accr.student.nutrition.details"
    _description = "Student Nutrition Details"
    
    student = fields.Many2one('x_student', string=u'Student', required=True, ondelete='set null', )
    name = fields.Char(related='student.display_name', string=u'Name', readonly=True, )
    age = fields.Integer(related='student.x_studio_age', string=u"Age", readonly=True, )
    diagnosis = fields.Text(related='student.x_studio_diagnosis', string=u'Diagnosis', readonly=True, )
    residential_section = fields.Many2one(related='student.x_studio_residential_sections', string=u'Residential Section', readonly=True, )
    medications = fields.One2many(related='student.x_studio_field_jm5yW', string=u'Medications', readonly=True, )
    food_preferences = fields.One2many('accr.food.preferences', 'student_nutrition_details', string=u'Food Preferences', )

    height = fields.Integer(string=u'Height', required=True, )
    weight = fields.Integer(string=u'Weight', required=True, )
    diet = fields.Char(string=u'Diet', )
    requirements = fields.Char(string=u'Requirements', )
    physical_activity = fields.Char(string=u'Physical Activity', )
    water_intake = fields.Char(string=u'Water Intake', )