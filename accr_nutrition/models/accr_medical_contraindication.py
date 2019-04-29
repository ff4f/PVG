from odoo import models, fields, api,  _

class accrMedicalContraindication(models.Model):

    _name = "accr.medical.contraindication"
    _description = "ACCR Medical Contraindication"

    name = fields.Char(string=u'Name', required=True)
    medicines = fields.Many2many('accr.medical.unit.medicine', 'accr_medical_contraindication_medicines_rel', 'contraindication_id', 'medicine_id', string=u'Medicines')
    food_types = fields.Many2many('accr.food.type', 'accr_medical_contraindication_food_type_rel', 'contraindication_id', 'food_type_id', string=u'Food Types')