from odoo import models, fields, _

class accrMedicalUnitmedicineSideEffects(models.Model):

    _name = "accr.medical.unit.medicine.side.effects"
    _description = "ACCR Medical Unit Medicines Side Effects"

    name = fields.Char(string=u'Medicine Side Effect')
    symptoms = fields.Text(string=u'Symptoms')
    medicines = fields.Many2many('accr.medical.unit.medicine', 'accr_medical_unit_medicines_side_effects_rel', 'side_effects_id', 'medicine_id', string=u'medicines')