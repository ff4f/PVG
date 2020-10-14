# -*- coding: utf-8 -*-
###############################################################################
#
#
###############################################################################

from odoo import models, fields, api, _


class EDUSubject(models.Model):
    _name = "edu.subject"
    _description = "Subject"

    name = fields.Char('Name', size=128, required=True)
    grade_weightage = fields.Float('Grade Weightage')
    subject_type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        'Subject Type', default="compulsory", required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_subject_name',
         'unique(name)', 'Code should be unique per subject!'),
    ]
