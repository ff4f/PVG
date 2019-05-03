from odoo import models, fields

class accrBCABMR(models.Model):
    _name = 'accr.bca.bmr'

    bmr = fields.Char(string=u"BMR", required=True)