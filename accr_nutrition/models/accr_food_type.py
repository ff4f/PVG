from odoo import models, fields

class accrFoodType(models.Model):
    _name = "accr.food.type"
    _description = "ACCR Food Types"

    name = fields.Char(string="Food Type",)
    # medical_contraindication = fields.Many2many('accr.food.type', 'accr_medical_contraindication_food_type_rel', 'food_type_id', 'medicine_id', string=u'Medicines')