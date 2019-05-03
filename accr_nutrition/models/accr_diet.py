from odoo import models, fields

class accrDiet(models.Model):
    _name = 'accr.diet'
    _sql_constraints = [('student_unique', 'unique(students)', 'Can not be duplicate value for this field!')]

    name = fields.Char(string=u'Diet', required=True,)
    students = fields.Many2many('x_student', 'x_student_diet_rel',
                                'diet_id', 'x_student_id', string="Students", required=False, )