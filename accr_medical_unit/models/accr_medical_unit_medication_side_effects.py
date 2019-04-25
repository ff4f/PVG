from odoo import models, fields, _

class accrMedicalUnitMedicationSideEffects(models.Model):

    _name = "accr.medical.unit.medication.side.effects"
    _description = "ACCR Medical Unit Medications Side Effects"

    name = fields.Char(string=u'Medicaiton Side Effect')
    symptoms = fields.Text(string=u'Symptoms')
    medications = fields.Many2many('accr.medical.unit.medication', 'accr_medical_unit_medications_side_effects_rel', 'side_effects_id', 'medication_id', string=u'Medications')