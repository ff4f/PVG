from odoo import models, fields, api,  _


class accrMedicalUnitMedicine(models.Model):

    _name = "accr.medical.unit.medicine"
    _description = "ACCR Medical Unit Medicines"

    name = fields.Char(string=u'Medicine')
    discription = fields.Text(string=u'Description')
    alternetive_medicines = fields.Many2many('accr.medical.unit.medicine', 'accr_medical_unit_medicines_rel',
                                               'medicine_1_id', 'medicine_2_id', string=u'Alternetive Medicines')
    side_effects = fields.Many2many('accr.medical.unit.medicine.side.effects',
                                    'accr_medical_unit_medicines_side_effects_rel', 'medicine_id', 'side_effects_id', string=u'Side Effects')

