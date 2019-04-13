from datetime import datetime
from datetime import timedelta

from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

from odoo import models, fields, api, _


class SessionReport(models.TransientModel):
    _name = "accr.time.table.report"
    _description = "Generate Time Table Report"

    section = fields.Many2one(
        'x_student_residential_sections', 'Section', required=True)
    start_date = fields.Date(
        'Start Date', required=True,
        default=(datetime.today() - relativedelta(
            days=datetime.date(
                datetime.today()).weekday())).strftime('%Y-%m-%d'))
    end_date = fields.Date(
        'End Date', required=True,
        default=(datetime.today() + relativedelta(days=6 - datetime.date(
            datetime.today()).weekday())).strftime('%Y-%m-%d'))
    timing_type = fields.Selection(
        [('academic', 'Academic'), ('non-academic', 'Non-Academic'), ('all', 'All')], 'Type', required=True)

    @api.multi
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for session in self:
            start_date = fields.Date.from_string(session.start_date)
            end_date = fields.Date.from_string(session.end_date)
            if end_date < start_date:
                raise ValidationError(_('End Date cannot be set before \
                Start Date.'))
            elif end_date > (start_date + timedelta(days=6)):
                raise ValidationError(_("Select date range for a week!"))

    @api.multi
    def gen_time_table_report(self):
        template = self.env.ref(
            'accr_scheduler.report_timetable_generate')
        data = self.read(
            ['start_date', 'end_date', 'section', 'timing_type'])[0]
        timing_type = self.timing_type
        if timing_type == 'all':
            time_table_ids = self.env['accr.session'].search(
                [('section', '=', data['section'][0]),
                 ('start_datetime', '>=', data['start_date']),
                 ('end_datetime', '<=', data['end_date'])],
                order='start_datetime asc')
            data.update({'time_table_ids': time_table_ids.ids})
        elif timing_type == 'academic':
            time_table_ids = self.env['accr.session'].search(
                [('section', '=', data['section'][0]),
                 ('start_datetime', '>=', data['start_date']),
                 ('end_datetime', '<=', data['end_date']),
                 ('timing_type', '=', 'academic')],
                order='start_datetime asc')
            data.update({'time_table_ids': time_table_ids.ids})
        elif timing_type == 'non-academic':
            time_table_ids = self.env['accr.session'].search(
                [('section', '=', data['section'][0]),
                 ('start_datetime', '>=', data['start_date']),
                 ('end_datetime', '<=', data['end_date']),
                 ('timing_type', '=', 'non-academic')],
                order='start_datetime asc')
            data.update({'time_table_ids': time_table_ids.ids})
        # time_table_ids = self.env['accr.session'].search(
        #         [('section', '=', data['section'][0]),
        #          ('start_datetime', '>=', data['start_date']),
        #          ('end_datetime', '<=', data['end_date']),
        #          ('timing_type', '=', data['timing_type'])],
        #         order='start_datetime asc')
        # data.update({'time_table_ids': time_table_ids.ids})
        return template.report_action(self, data=data)
