from odoo import models, fields

class accrBCA(models.Model):
    _name = 'accr.bca'

    ideal_weight = fields.Float(string=u"Ideal weight")
    actual_weight = fields.Float(string=u"Actual weight")
    bmr = fields.Many2one('accr_bca_bmr', string=u"BMR")
    fat_kg = fields.Float(string=u"FAT.kg")
    fat_percentage = fields.Integer(string=u"FATS.%")
    mucles_kg = fields.Float(string=u"Mucles.kg")
    lean_muscles = fields.Integer(string=u"Lean Muscles")
    fat_control_kg = fields.Float(string=u"Fat Control.KG")
    muscles_control_kg = fields.Float(string=u"Muscles Control.KG")
    icw = fields.Integer(string=u"ICW")
    ecw = fields.Integer(string=u"ECW")

    nutrition_student = fields.Many2one('accr.nutrition.student', string=u"Student")
    student = fields.Many2one(related='nutrition_student.student', string=u"Student")