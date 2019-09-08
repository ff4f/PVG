# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HrAppraisal(models.Model):
    _inherit = "hr.appraisal"

    manager_survey_goal = fields.Integer('Goal Percentage')
    colleagues_survey_goal = fields.Integer('Goal Percentage')
    employee_survey_goal = fields.Integer('Goal Percentage')
    collaborators_survey_goal = fields.Integer('Goal Percentage')

    @api.onchange('employee_id')
    def onchange_employee_id(self):
        if self.employee_id:
            self.department_id = self.employee_id.department_id
            self.manager_appraisal = self.employee_id.appraisal_by_manager
            self.manager_ids = self.employee_id.appraisal_manager_ids
            self.manager_survey_id = self.employee_id.appraisal_manager_survey_id
            self.colleagues_appraisal = self.employee_id.appraisal_by_colleagues
            self.colleagues_ids = self.employee_id.appraisal_colleagues_ids
            self.colleagues_survey_id = self.employee_id.appraisal_colleagues_survey_id
            self.employee_appraisal = self.employee_id.appraisal_self
            self.employee_survey_id = self.employee_id.appraisal_self_survey_id
            self.collaborators_appraisal = self.employee_id.appraisal_by_collaborators
            self.collaborators_ids = self.employee_id.appraisal_collaborators_ids
            self.collaborators_survey_id = self.employee_id.appraisal_collaborators_survey_id
            self.manager_survey_goal = self.employee_id.appraisal_manager_survey_goal
            self.colleagues_survey_goal = self.employee_id.appraisal_colleagues_survey_goal
            self.employee_survey_goal = self.employee_id.appraisal_self_survey_goal
            self.collaborators_survey_goal = self.employee_id.appraisal_collaborators_survey_goal
