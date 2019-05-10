from odoo import models, fields

class accrMIN(models.Model):
    _name = 'accr.nutrition.min'

    name = fields.Char(string=u"MIN", required=True)