from odoo import models, fields


class accrStudentFoodPreferences(models.Model):
    _name = "accr.food.preferences"
    _description = "Food prefernces menu for student"

    student = fields.Many2one('x_student', string=u'Student', required=True, ondelete='set restrict', )
    student_nutrition_details = fields.Many2one('accr.student.nutrition.details', string=u'Nutrition Details',)
    name = fields.Char('Name', required=True,)
    preference = fields.Selection(
        [('Like', 'Like'), ('Dislike', 'Dislike')], string=u'Preference', required=True,)
    intolerance = fields.Boolean(string=u'Intolerance',)
