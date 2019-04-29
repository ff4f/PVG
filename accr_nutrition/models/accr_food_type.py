from odoo import models, fields

class accrFoodType(models.Model):
    _name = "accr.food.type"
    _description = "ACCR Food Types"

    name = fields.Char(string="Food Type", required=True, )