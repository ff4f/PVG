# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MonthlyPlans(models.Model):
    _name = 'monthly.plans'
    _inherit = ["mail.thread"]
    _rec_name = 'teacher_id'

    month = fields.Char()
    student_id = fields.Many2one("x_student", string="Student", required=True)
    teacher_id = fields.Many2one(comodel_name="res.users", string="Teacher", required=True, )
    date_from = fields.Date(string="Date From", required=False, )
    date_to = fields.Date(string="Date To", required=False, )
    line_ids = fields.One2many(comodel_name="monthly.plans.lines", inverse_name="plan_id" )

class PlansLines(models.Model):
    _name = 'monthly.plans.lines'

    teach_goal_id = fields.Many2one('x_se_plan_long_term_goals',string="Goal")
    comment = fields.Char(string="Comment")
    is_accomplished = fields.Boolean('Accomplished')
    not_accomplished = fields.Boolean('Not Accomplished')
    plan_id = fields.Many2one(comodel_name="monthly.plans", string="", required=False, )