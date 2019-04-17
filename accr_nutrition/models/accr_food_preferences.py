from odoo import models, fields, api, _


class accrStudentFoodPreferences(models.Model):
    _name = "accr.food.preferences"
    _description = "Food prefernces menu for student"

    student = fields.Many2one(
        'x_student', string=u'Student', required=True, ondelete='set null', )
    student_nutrition_details = fields.Many2one(
        'accr.student.nutrition.details', string=u'Nutrition Details',)
    food = fields.Many2one('accr.food', string=u'Food',
                           required=True, ondelete='set null', )
    name = fields.Char('Name', compute='_compute_name', )
    preference = fields.Selection(
        [('Like', 'Like'), ('Dislike', 'Dislike')], string=u'Preference', required=True,)

    @api.multi
    @api.depends('student', 'food')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - ' + record.food.display_name
