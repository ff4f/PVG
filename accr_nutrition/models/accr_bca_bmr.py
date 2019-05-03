from odoo import models, fields

class accrBCA_BMR(models.Model):
    _name = 'accr.bca.bmr'

    bmr = fields.Char(string=u"BMR", required=True)