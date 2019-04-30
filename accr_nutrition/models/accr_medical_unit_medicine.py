from odoo import models, fields, api,  _


class accrMedicalUnitMedicine(models.Model):

    _inherit = "accr.medical.unit.medicine"

    medical_contraindication = fields.Many2many('accr.medical.unit.medicine', 'accr_medical_contraindication_medicines_rel', 'medicine_id', 'contraindication_id', string=u'Medical Contraindication', required=True)