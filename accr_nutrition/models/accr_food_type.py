from odoo import models, fields

class accrFoodType(models.Model):
    _name = "accr.food.type"
    _description = "ACCR Food Types"

    name = fields.Char(string="Food Type", required=True, )
    food = fields.One2many('accr.food', 'food_type', string=u'Food', )
    medical_contraindication = fields.Many2many('accr.medical.contraindication', 'accr_medical_contraindication_food_type_rel', 'food_type_id', 'contraindication_id', string=u'Food Types', required=True)