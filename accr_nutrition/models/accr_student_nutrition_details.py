import datetime
from odoo import models, fields, api, _


class accrStudentNutritionDetails(models.Model):
    _name = "accr.student.nutrition.details"
    _description = "Student Nutrition Details"

    name = fields.Char(compute='_compute_name', string=u'Name', readonly=True, )
    
    diet = fields.Many2one('accr.diet', string=u'Current Diet', required=True, copy=True, )

    # Nutritional Needs
    needs_cho = fields.Integer(string=u"CHO %", copy=True, )
    needs_pro = fields.Integer(string=u"PRO %", copy=True, )
    needs_fats = fields.Integer(string=u"FATS %", copy=True, )
    needs_vit = fields.Many2one('accr.nutrition.vit', string=u"VIT", copy=True, )
    needs_min = fields.Many2one('accr.nutrition.min', string=u"MIN", copy=True, )
    needs_wi = fields.Float(string=u"Water Intake .L")

    # Nutritional Requirements KCAL per day: INTEGER
    requirement_kcal = fields.Integer(string=u"Requirement KCAL per day", copy=True, )

    sleep_hours = fields.Integer(string=u"Sleep Hours", copy=True, )
    physical_activity = fields.Many2one('accr.physical.activity', string=u'Physical Activity', copy=True, )
    physiothrtapy = fields.Char(string=u"Physiothrtapy", copy=True, )
    activity_level = fields.Many2one("accr.activity.level", string=u"Activity.level", copy=True, )
    meal_frequency = fields.Integer(string=u"Meal Frequency", copy=True, )
    food_textures = fields.Many2one('accr.food.textures', string=u'Textures of food', copy=True, )
    habits = fields.Char(string=u"Habits", copy=True, )
    others = fields.Text(string=u"Others", copy=True, )

    date = fields.Date(string=u"Date", required=True, )
    
    nutrition_student = fields.Many2one('accr.nutrition.student', string=u'Student', copy=True, )
    student = fields.Many2one(related='nutrition_student.student', string=u'X Student', )

    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - '+ record.create_date.strftime("%Y-%m-%d")

    # @api.multi
    # @api.depends('diet')
    # def _compute_student_diet(self):
    #     for record in self:
    #         if record.diet:
    #             record.nutrtition_student_diet = record.diet

            

    # @api.onchange('diet')	
    # def _add_student_to_diet(self):
    #     for record in self:
    #         if record.student:
    #             diet = self.env['accr.diet'].search([('id','=',record.diet.id)])
    #             if diet and record.student:
    #                 diet.write({'students': [(0, 0, {'diet_id': diet.id, 'x_student_id': record.student.id})]})

    # @api.onchange('diet')
    # def _change_student_diet(self):
    #     self.nutrition_student.diet = self.diet