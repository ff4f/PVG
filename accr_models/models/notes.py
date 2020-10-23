# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NotesDirections(models.Model):
    _name = 'notes.directions'
    _inherit = ["mail.thread"]
    _rec_name = 'teacher_id'

    teacher_id = fields.Many2one(comodel_name="res.users", string="Teacher", required=True, )
    week_list = fields.Selection([
        ('MO', 'Monday'),
        ('TU', 'Tuesday'),
        ('WE', 'Wednesday'),
        ('TH', 'Thursday'),
        ('FR', 'Friday'),
        ('SA', 'Saturday'),
        ('SU', 'Sunday')
    ], string='Weekday')
    date = fields.Date(string="Date", required=False, )
    notesdirections_ids = fields.One2many(comodel_name="notes.directions.lines", inverse_name="notesdirections", string="", required=False, )

class NotesDirectionsLines(models.Model):
    _name = 'notes.directions.lines'

    item = fields.Char(string="Item", required=False, )
    type = fields.Char(string="Notes and directions", required=False, )
    notesdirections = fields.Many2one(comodel_name="notes.directions", string="", required=False, )