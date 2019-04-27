from odoo import models, fields, api,  _


class accrMedicalUnitMedication(models.Model):

    _name = "accr.medical.unit.medication"
    _description = "ACCR Medical Unit Medication"

    name = fields.Char(string=u'Medication', compute='_compute_name')
    medicine = fields.Many2one('accr.medical.unit.medicine', string=u'Medicine')
    discription = fields.Text(string=u'Description')
    dose = fields.Integer(string=u'Dose')
    frequency = fields.Integer(string=u'Frequency/Day')
    duration = fields.Integer(string=u'Duration')
    duration_type = fields.Selection(string=u'-', selection=[('days', 'Days'), ('weeks', 'weeks'), ('months', 'Months')])

    @api.multi
    @api.depends('start_datetime')
    def _compute_name(self):
        for record in self:
            if record.medicine:
                record.name = record.medicine.name
