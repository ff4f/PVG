# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WeeklyPlans(models.Model):
    _name = 'weekly.plans'
    _inherit = ["mail.thread"]
    _rec_name = 'teacher_id'

    teacher_id = fields.Many2one(comodel_name="res.users", string="Teacher", required=True, )
    date_from = fields.Date(string="Date From", required=False, )
    date_to = fields.Date(string="Date To", required=False, )
    weekly_plans_ids = fields.One2many(comodel_name="weekly.plans.lines", inverse_name="weekly_plans", string="", required=False, )

class WeeklyPlansLines(models.Model):
    _name = 'weekly.plans.lines'

    type = fields.Char(string="Type", required=False, )
    activity_type = fields.Char(string="Activity Type", required=False, )
    goal = fields.Char(string="Goal", required=False, )
    weekly_plans = fields.Many2one(comodel_name="weekly.plans", string="", required=False, )