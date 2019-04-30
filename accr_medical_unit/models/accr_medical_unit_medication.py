from odoo import models, fields, api,  _


class accrMedicalUnitMedication(models.Model):

    _name = "accr.medical.unit.medication"
    _description = "ACCR Medical Unit Medication"

    name = fields.Char(string=u'Medication', compute='_compute_name')
    medicine = fields.Many2one('accr.medical.unit.medicine', string=u'Medicine', required=True, )
    discription = fields.Text(string=u'Description')
    dose = fields.Integer(string=u'Dose/mg', required=True,)
    frequency = fields.Integer(string=u'Frequency/Day', required=True,)

    # duration = fields.Integer(string=u'Duration', required=True,)
    # duration_type = fields.Selection(string=u'-', selection=[('days', 'Days'), ('weeks', 'weeks'), ('months', 'Months')])

    start_date_time = fields.Datetime(string=u'Start Time', required=True,)
    end_date_time = fields.Datetime(string=u'End Time', required=True,)

    x_medical_medications = fields.Many2one('x_medical_medications', string='x_medical_medications', required=True, )
    medicaiotn_student = fields.Many2one(related='x_medical_medications.x_studio_student', string=u"Student", store=False,  )
    student = fields.Many2one('x_student', string=u'Student', compute='_compute_student', required=True, )

    @api.multi
    @api.depends('medicine')
    def _compute_name(self):
        for record in self:
            if record.medicine:
                record.name = record.medicine.name

    # @api.multi
    # @api.depends('medicaiotn_student')
    # def _compute_student(self):
    #     for record in self:
    #         if record.medicaiotn_student:
    #             record.name = record.medicaiotn_student.id

    @api.multi
    @api.depends('x_medical_medications')
    def _compute_student(self):
        for record in self:
            if record.x_medical_medications:
                record.name = record.x_medical_medications.x_studio_student.id
