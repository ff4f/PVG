from odoo import models, fields

class accrWaterIntake(models.Model):
    _name = 'accr.water.intake'

    name = fields.Char(string=u'Water Intake')