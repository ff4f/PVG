from odoo import models, fields

class accrStudent(models.Model):
    _name = 'x_student'
    _inherit = ['x_student']

    diet = students = fields.Many2many('x_student', 'x_student_diet_rel', 'x_student_id', 'diet_id', string="Diets", )
    food_intolerance = fields.One2many('accr.student.food.intolerance', 'student', string=u'Food Intolerance', )          
    food_preferences = fields.One2many('accr.student.food.preferences', 'student', string=u'Food Preferences', )                      
    nutrition_details = fields.One2many('accr.student.nutrition.details', 'student', string=u'Nutrition Details', )
    