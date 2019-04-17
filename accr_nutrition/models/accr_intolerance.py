from odoo import models, fields

class accrIntoleranceFoodType(models.Model):
    _name = "accr.intolerance"

    name = fields.Char(string="Food Type",)