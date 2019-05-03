from odoo import models, fields

class accrBCABMR(models.Model):
    _name = 'accr.bca.bmr'

    name = fields.Char(string=u"BMR", required=True)