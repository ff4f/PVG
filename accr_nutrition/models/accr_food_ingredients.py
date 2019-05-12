from odoo import models, fields

class accrFoodType(models.Model):
    _name = "accr.food.ingredients"
    _description = "ACCR Food Ingredientss"

    name = fields.Char(string="Food Ingredients", required=True, )
    food = fields.One2many('accr.food', 'food_ingredients', string=u'Food', )
    medical_contraindication = fields.Many2many('accr.medical.contraindication', 'accr_medical_contraindication_food_ingredients_rel', 'food_ingredients_id', 'contraindication_id', string=u'Food Ingredientss', required=True)