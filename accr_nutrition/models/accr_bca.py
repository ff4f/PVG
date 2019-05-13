from odoo import models, fields, api

class accrBCA(models.Model):
    _name = 'accr.bca'

    name = fields.Char(string=u"Name", compute="_compute_name")
    report_name = fields.Char(string=u"Report Name", compute="_compute_report_name")
    height = fields.Integer(string=u"Height.cm", )
    ideal_weight = fields.Float(string=u"Ideal weight.kg")
    actual_weight = fields.Float(string=u"Actual weight.kg")
    bmr = fields.Many2one('accr.bca.bmr', string=u"BMR")
    fat_kg = fields.Float(string=u"FAT.kg")
    fat_percentage = fields.Float(string=u"FATS.%")
    mucles_kg = fields.Float(string=u"Mucles.kg")
    lean_muscles = fields.Float(string=u"Lean Muscles.kg")
    fat_control_kg = fields.Float(string=u"Fat Control.KG")
    muscles_control_kg = fields.Float(string=u"Muscles Control.KG")
    icw = fields.Float(string=u"ICW.L")
    icw_normal_range = fields.Char(string=u"Normal Range", )
    ecw = fields.Float(string=u"ECW.L")
    ecw_normal_range = fields.Char(string=u"Normal Range", )
    bmi = fields.Float(string=u"BMI")
    weight_control = fields.Float(string=u"Weight Control.kg", )

    nutrition_student = fields.Many2one('accr.nutrition.student', string=u"Student")
    student = fields.Many2one(related='nutrition_student.student', string=u"X Student")

    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.student:
                record.name = record.student.display_name + ' - ' + record.create_date.strftime("%Y-%m-%d")

    @api.multi
    @api.depends('create_date')
    def _compute_report_name(self):
        for record in self:
            record.report_name = record.create_date.strftime("%Y_%m_%d")
