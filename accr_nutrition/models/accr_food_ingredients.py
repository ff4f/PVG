from odoo import models, fields

class accrFoodType(models.Model):
    _name = "accr.food.ingredients"
    _description = "ACCR Food Ingredientss"

    name = fields.Char(string="Food Ingredients", required=True, )
    food = fields.Many2many('accr.food', 'accr_food_ingredients_food_rel', 'food_id', 'food_ingredients_id', string=u'Food', required=True, )
    medical_contraindication = fields.Many2many('accr.medical.contraindication', 'accr_medical_contraindication_food_ingredients_rel', 'food_ingredients_id', 'contraindication_id', string=u'Food Ingredientss', required=True)