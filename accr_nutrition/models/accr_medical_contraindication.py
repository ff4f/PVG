from odoo import models, fields, api,  _

class accrMedicalContraindication(models.Model):

    _name = "accr.medical.contraindication"
    _description = "ACCR Medical Contraindication"

    name = fields.Char(string=u'Name', required=True)
    medicines = fields.Many2many('accr.medical.unit.medicine', 'accr_medical_contraindication_medicines_rel', 'contraindication_id', 'medicine_id', string=u'Medicines', required=True)
    food_ingredientss = fields.Many2many('accr.food.ingredients', 'accr_medical_contraindication_food_ingredients_rel', 'contraindication_id', 'food_ingredients_id', string=u'Food Ingredientss', required=True)