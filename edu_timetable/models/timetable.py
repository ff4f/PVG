# -*- coding: utf-8 -*-
###############################################################################
#
###############################################################################

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


class EDUTimetable(models.Model):
    _name = "edu.timetable"
    _inherit = ["mail.thread"]
    _description = "Timetable"

    name = fields.Char(string='Name', required=True, copy=False, store=True, index=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('time'))
    class_room_id = fields.Many2one('x_student_class_room',string='Class Room')
    user_id = fields.Many2one('res.users', string='Representative', default= lambda self: self.env.user)
    start_date = fields.Date(
        'Start Time', required=True,copy=True)
    end_date = fields.Date(
        'End Time', required=True,copy=True)
    color = fields.Integer('Color Index',copy=True)
    line_ids = fields.One2many('edu.timetable.item','timetable_id',string='Lines',copy=True)


    @api.constrains('start_date', 'end_date')
    def _check_date_time(self):
        if self.start_date > self.end_date:
            raise ValidationError(_(
                'End Time cannot be set before Start Time.'))


class EDUTimetableLine(models.Model):
    _name = "edu.timetable.item"


    subject_id = fields.Many2one('edu.subject',string='Subject')
    dayofweek = fields.Selection([
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ], 'Day of Week', required=True, index=True, default='Saturday',copy=True)
    hour_from = fields.Float(string='Work from', required=True, index=True,
                             help="Start and End time of working.\n"
                                  "A specific value of 24:00 is interpreted as 23:59:59.999999.",copy=True)
    hour_to = fields.Float(string='Work to', required=True,copy=True)
    student_ids = fields.Many2many('x_student',string='Students',copy=True)
    timetable_id = fields.Many2one("edu.timetable", string="Timetable", required=True, ondelete='cascade')
    start_date = fields.Date(
        'Start Time',related='timetable_id.start_date',store=True)
    end_date = fields.Date(
        'End Time',related='timetable_id.end_date',store=True)
