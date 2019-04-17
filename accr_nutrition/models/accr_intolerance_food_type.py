from odoo import models, fields

class accrIntoleranceFoodType(models.Model):
    _name = "accr.intolerance.food.type"

    name = fields.Char(string="Food Type",)