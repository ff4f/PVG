from odoo import models, fields

class accrDiet(models.Model):
    _name = 'accr.diet'

    name = fields.Char(string=u'Diet', required=True,)
    students = fields.One2many('accr.nutrition.student', 'diet', string="Students", required=False, )