from odoo import models, fields

class accrXMedicalMedications(models.Model):
    _inherit = 'x_medical_medications'

    medication_records = fields.One2many('accr.medical.unit.medication', 'x_medical_medications', string=u'Medication Records')

