from odoo import models, fields, api, _

class accrStudentFoodIntolerance(models.Model):
    _name = "accr.student.food.intolerance"

    food_ingredients = fields.Many2one('accr.food.ingredients', string=u'Food Ingredients', required=True, )
    # nutrition_details = fields.Many2one('accr.student.nutrition.details', string=u'Nutrition Details' )
    # student = fields.Many2one('x_student', string=u'Student', required=True, )
    nutrition_student_food_intolerance = fields.Many2one('accr.nutrition.student', string=u'Student', )
    nutrition_student_medical_contraindication = fields.Many2one('accr.nutrition.student', string=u'Student', )
    food = fields.One2many(related='food_ingredients.food', string=u'Food', )
    

    @api.multi
    @api.depends('student', 'food_ingredients')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - ' + record.food_ingredients.display_name
