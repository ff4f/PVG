from odoo import models, fields

class accrDiet(models.Model):
    _name = 'accr.diet'

    name = fields.Char(string=u'Diet')
    students = fields.Many2many('x_student', 'x_student_diet_rel',
                                'diet_id', 'x_student_id', string="Students", required=True, )