from odoo import models, fields, api,  _


class accrMedicalUnitMedication(models.Model):

    _name = "accr.medical.unit.medication"
    _description = "ACCR Medical Unit Medication"

    name = fields.Char(string=u'Medication', compute='_compute_name')
    medicine = fields.Many2one('accr.medical.unit.medicine', string=u'Medicine', required=True, )
    discription = fields.Text(string=u'Description')
    dose = fields.Integer(string=u'Dose/mg', required=True,)
    frequency = fields.Integer(string=u'Frequency/Day', required=True,)
    duration = fields.Integer(string=u'Duration', required=True,)
    duration_type = fields.Selection(string=u'-', selection=[('days', 'Days'), ('weeks', 'weeks'), ('months', 'Months')])
    x_medical_medications = fields.Many2one('x_medical_medications', string='x_medical_medications')
    x_medical_assessment = fields.Many2one('x_medical_assessment', string='x_medical_assessment')

    @api.multi
    @api.depends('medicine')
    def _compute_name(self):
        for record in self:
            if record.medicine:
                record.name = record.medicine.name
