from odoo import models, fields

class accrPhysicalActivity(models.Model):
    _name = 'accr.physical.activity'

    name = fields.Char(string=u'Physical Activity', required=True, )