from odoo import models, fields, _

class accrMedicalUnitMedication(models.Model):

    _name = "accr.medical.unit.medication"
    _description = "ACCR Medical Unit Medications"

    name = fields.Char(string=u'Medicaiton')
    discription = fields.Text(string=u'Description')
    alternetive_medicaiotn = fields.Many2one('accr.medical.unit.medication', string=u'Alternetive Medication')
    alternetive_medications = fields.One2many('accr.medical.unit.medication', 'alternetive_medicaiotn', string=u'Alternetive Medications')
    side_effects = fields.Many2many('accr.medical.unit.medication.side.effects', 'accr_medical_unit_medications_side_effects_rel', 'medication_id', 'side_effects_id', string=u'Side Effects')