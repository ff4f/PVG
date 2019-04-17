from odoo import models, fields, api, _


class accrMealTiming(models.Model):
    _name = "accr.meal.timing"
    _description = "Meal Timing"

    name = fields.Char('Name', required=True)
    hour = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
         ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
         ('11', '11'), ('12', '12')], 'Hours', required=True)
    minute = fields.Selection(
        [('00', '00'), ('15', '15'), ('30', '30'), ('45', '45')], 'Minute',
        required=True)
    duration = fields.Float('Duration')
    am_pm = fields.Selection(
        [('am', 'AM'), ('pm', 'PM')], 'AM/PM', required=True)
    
    meal_type = fields.Many2one('accr.meal.type', string=u"Meal Type", required=True, )
    food = fields.Many2many('accr.food','accr_food_meal_timing_rel', 'accr_meal_timing_id', 'accr_food_id', string="Food", required=True, )

    @api.multi
    @api.depends('meal_type', 'hour', 'minute')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - ' + record.hour.value + ':'+ record.minute.value
