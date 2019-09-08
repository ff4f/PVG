from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    appraisal_manager_survey_goal = fields.Integer('Goal Percentage')
    appraisal_colleagues_survey_goal = fields.Integer('Goal Percentage')
    appraisal_self_survey_goal = fields.Integer('Goal Percentage')
    appraisal_collaborators_survey_goal = fields.Integer('Goal Percentage')
