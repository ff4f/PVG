import calendar
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

week_days = [(calendar.day_name[0], _(calendar.day_name[0])),
             (calendar.day_name[1], _(calendar.day_name[1])),
             (calendar.day_name[2], _(calendar.day_name[2])),
             (calendar.day_name[3], _(calendar.day_name[3])),
             (calendar.day_name[4], _(calendar.day_name[4])),
             (calendar.day_name[5], _(calendar.day_name[5])),
             (calendar.day_name[6], _(calendar.day_name[6]))]


class accrMealTimetable(models.Model):
    _name = "accr.meal.timetable"
    _description = "Meal Timetable"

    name = fields.Char(compute='_compute_name', string=u'Name', store=True)
    meal_id = fields.Many2one(
        'accr.meal.timing', string=u'Meal', required=True, track_visibility="onchange")
    meal_type = fields.Many2one(
        related='meal_id.meal_type', string=u"Meal Type", readonly=True, store=False, )
    meal_type_food = fields.Many2many(related='meal_id.food', string=u"Food", readonly=True, store=False, )
    food = fields.Many2many('accr.food', 'meal_timetable_food_rel', 'meal_timetable_id', 'food_id', string="Food", required=True,  compute='_compute_food')                            
    start_datetime = fields.Datetime(
        string=u'Start Time', required=True,
        default=lambda self: fields.Datetime.now())
    end_datetime = fields.Datetime(
        string=u'End Time', required=True)
    type = fields.Char(compute='_compute_day', string=u'Day', store=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirmed'),
         ('done', 'Done'), ('cancel', 'Canceled')],
        'Status', default='draft')
    notes = fields.Text(string=u'Notes')
    diet = fields.Many2one('accr.diet', string=u'Diet', required=True,)
    students = fields.One2many(related='diet.students', string=u"Students", required=True, readonly=True, )
    student = fields.Many2one('accr.nutrition.student', string=u'Student')

    @api.multi
    @api.depends('start_datetime')
    def _compute_day(self):
        for record in self:
            record.type = fields.Datetime.from_string(
                record.start_datetime).strftime("%A")

    @api.multi
    @api.depends('start_datetime')
    def _compute_name(self):
        for record in self:
            if record.meal_id and record.start_datetime:
                record.name = str(record.meal_id.name)

    @api.multi
    def lecture_draft(self):
        self.state = 'draft'

    @api.multi
    def lecture_confirm(self):
        self.state = 'confirm'

    @api.multi
    def lecture_done(self):
        self.state = 'done'

    @api.multi
    def lecture_cancel(self):
        self.state = 'cancel'

    @api.constrains('start_datetime', 'end_datetime')
    def _check_date_time(self):
        if self.start_datetime > self.end_datetime:
            raise ValidationError(_(
                'End Time cannot be set before Start Time.'))

    
    @api.multi
    @api.depends('meal_type')
    def _compute_food(self):
        for record in self:
            foods = []
            for food in record.meal_type.food:
                foods.append(food.id)
            record.food = [(6, 0, foods)]
                
