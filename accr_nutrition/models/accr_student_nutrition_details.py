import datetime
from odoo import models, fields, api, _


class accrStudentNutritionDetails(models.Model):
    _name = "accr.student.nutrition.details"
    _description = "Student Nutrition Details"

    name = fields.Char(compute='_compute_name', string=u'Name', readonly=True, )
    
    diet = fields.Many2one('accr.diet', string=u'Diet', required=True, )

    # Nutritional Needs
    needs_cho = fields.Integer(string=u"CHO")
    needs_pro = fields.Integer(string=u"PRO")
    needs_fats = fields.Integer(string=u"FATS")
    needs_vit = fields.Char(string=u"VIT")
    needs_min = fields.Char(string=u"MIN")
    needs_wi = fields.Float(string=u"Water Intake")

    # Nutritional Requirements KCAL per day: INTEGER
    requirement_kcal = fields.Integer(string=u"Requirement KCAL per day")

    sleep_hours = fields.Integer(string=u"Sleep Hours")
    physical_activity = fields.Many2one('accr.physical.activity', string=u'Physical Activity', )
    physiothrtapy = fields.Char(string=u"Physiothrtapy")
    activity_level = fields.Char(string=u"Activity.level")
    meal_frequency = fields.Integer(string=u"Meal Frequency")
    food_textures = fields.Many2one('accr.food.textures', string=u'Textures of food')
    habits = fields.Char(string=u"Habits")
    others = fields.Text(string=u"Others")
    
    nutrition_student = fields.Many2one('accr.nutrition.student', string=u'Student', )
    student = fields.Many2one(related='nutrition_student.student', string=u'X Student', )

    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - '+ record.create_date.strftime("%Y-%m-%d")

            

    @api.onchange('diet')	
    def _add_student_to_diet(self):
        for record in self:
            if record.student:
                diet = self.env['accr.diet'].search([('id','=',record.diet.id)])
                if diet and record.student:
                    diet.write({'students': [(0, 0, {'diet_id': diet.id, 'x_student_id': record.student.id})]})