from odoo import models, fields

class accrFood(models.Model):
    _name = 'accr.food'

    name = fields.Char(string=u'Food')