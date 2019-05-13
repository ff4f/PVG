from odoo import models, fields


class accrTiming(models.Model):
    _name = "accr.timing"
    _description = "Task Timing"
    _order = "sequence"

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
    sequence = fields.Integer('Sequence')
    timing_type = fields.Selection([('general', 'General'), ('nutrition', 'Nutrition'),  ('academic' , 'Academic'), ('non-academic', 'Non-Academic')], 'Type', required=True)
