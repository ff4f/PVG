from odoo import models, fields


class accrStudentFoodPreferences(models.Model):
    _name = "accr.food.preferences"
    _description = "Food prefernces menu for student"

    student = fields.Many2one(
        string=u'Student', comodel_name='model.x_student', ondelete='set restrict', required=True,)
    student_nutrition_details = fields.Many2one('accr.student.nutrition.details', 'Nutrition Details',)
    name = fields.Char('Name', required=True,)
    preference = fields.Selection(
        [('Like', 'Like'), ('Dislike', 'Dislike')], 'Preference', required=True,)
    intolerance = fields.Boolean(string=u'Intolerance',)
