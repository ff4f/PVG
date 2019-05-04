import calendar
import datetime
import pytz
import time

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class accrGenerateMealsTimeTable(models.TransientModel):
    _name = "accr.generate.meal.time.table"
    _description = "Generate Meals Timetable"

    time_table_lines = fields.One2many(
        'accr.gen.meal.time.table.line', 'gen_meal_time_table', 'Time Table Lines')
    time_table_lines_1 = fields.One2many(
        'accr.gen.meal.time.table.line', 'gen_meal_time_table', 'Time Table Lines1',
        domain=[('day', '=', '0')])
    time_table_lines_2 = fields.One2many(
        'accr.gen.meal.time.table.line', 'gen_meal_time_table', 'Time Table Lines2',
        domain=[('day', '=', '1')])
    time_table_lines_3 = fields.One2many(
        'accr.gen.meal.time.table.line', 'gen_meal_time_table', 'Time Table Lines3',
        domain=[('day', '=', '2')])
    time_table_lines_4 = fields.One2many(
        'accr.gen.meal.time.table.line', 'gen_meal_time_table', 'Time Table Lines4',
        domain=[('day', '=', '3')])
    time_table_lines_5 = fields.One2many(
        'accr.gen.meal.time.table.line', 'gen_meal_time_table', 'Time Table Lines5',
        domain=[('day', '=', '4')])
    time_table_lines_6 = fields.One2many(
        'accr.gen.meal.time.table.line', 'gen_meal_time_table', 'Time Table Lines6',
        domain=[('day', '=', '5')])
    time_table_lines_7 = fields.One2many(
        'accr.gen.meal.time.table.line', 'gen_meal_time_table', 'Time Table Lines7',
        domain=[('day', '=', '6')])
    start_date = fields.Date(
        'Start Date', required=True, default=time.strftime('%Y-%m-01'))
    end_date = fields.Date('End Date', required=True)
    diet = fields.Many2one('accr.diet', string=u'Diet', required=True,)
    students = fields.One2many(related='diet.students', string=u"Students", required=True, readonly=True, store=False )

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        start_date = fields.Date.from_string(self.start_date)
        end_date = fields.Date.from_string(self.end_date)
        if start_date > end_date:
            raise ValidationError(_("End Date cannot be set before \
            Start Date."))

    @api.multi
    def act_gen_meal_time_table(self):
        for record in self:
            start_date = record.start_date
            end_date = record.end_date

            for n in range((end_date - start_date).days + 1):
                curr_date = start_date + datetime.timedelta(n)
                for line in record.time_table_lines:
                    if int(line.day) == curr_date.weekday():
                        hour = line.meal_id.hour
                        if line.meal_id.am_pm == 'pm' and int(hour) != 12:
                            hour = int(hour) + 12
                        per_time = '%s:%s:00' % (hour, line.meal_id.minute)
                        final_date = datetime.datetime.strptime(
                            curr_date.strftime('%Y-%m-%d ') +
                            per_time, '%Y-%m-%d %H:%M:%S')
                        local_tz = pytz.timezone(
                            self.env.user.partner_id.tz or 'GMT')
                        local_dt = local_tz.localize(final_date, is_dst=None)
                        utc_dt = local_dt.astimezone(pytz.utc)
                        utc_dt = utc_dt.strftime("%Y-%m-%d %H:%M:%S")
                        curr_start_date = datetime.datetime.strptime(
                            utc_dt, "%Y-%m-%d %H:%M:%S")
                        curr_end_date = curr_start_date + datetime.timedelta(
                            hours=line.meal_id.duration)
                        for student in record.students:
                            self.env['accr.meal.timetable'].create({
                                'meal_id': line.meal_id.id,
                                'start_datetime':
                                curr_start_date.strftime("%Y-%m-%d %H:%M:%S"),
                                'end_datetime':
                                curr_end_date.strftime("%Y-%m-%d %H:%M:%S"),
                                'type': calendar.day_name[int(line.day)],
                                'diet': record.diet.id,
                                'student': student.id,
                                'diet': record.diet.id,
                                'color': 4,
                        })
            return {'type': 'ir.actions.act_window_close'}


class accrGenerateMealTimetableLine(models.TransientModel):
    _name = 'accr.gen.meal.time.table.line'
    _description = 'Generate Meal Time Table Lines'
    _rec_name = 'day'

    gen_meal_time_table = fields.Many2one(
        'accr.generate.meal.time.table', 'Meals Time Table', required=True)
    meal_id = fields.Many2one('accr.meal.timing', 'Meal Timing', required=True)
    day = fields.Selection([
        ('0', calendar.day_name[0]),
        ('1', calendar.day_name[1]),
        ('2', calendar.day_name[2]),
        ('3', calendar.day_name[3]),
        ('4', calendar.day_name[4]),
        ('5', calendar.day_name[5]),
        ('6', calendar.day_name[6]),
    ], 'Day', required=True)
