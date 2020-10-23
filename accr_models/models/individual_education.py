# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IndividualEducation(models.Model):
    _name = 'individual.education'
    _inherit = ["mail.thread"]
    _rec_name = 'student_id'

    student_id = fields.Many2one("x_student", string="Student", required=True)
    birthdate = fields.Date(string="Birth Date", required=False, )
    transdate = fields.Date(string="Date of conversion", required=False, )
    prepardate = fields.Date(string="Date of preparation of the program", required=False, )
    address = fields.Char(string="Address")
    manager_id = fields.Many2one(comodel_name="res.users", string="Manager")
    medical_diagnosis = fields.Char(string="Medical diagnosis", required=False, )
    contact_mobiles = fields.Integer(string="Parent Mobile", required=False, )
    nationality = fields.Many2one(comodel_name='res.country',string="Nationality")
    language = fields.Selection(string="Language", selection=[('arabic', 'Arabic'), ('english', 'English'), ], required=False, )
    lines_ids = fields.One2many(comodel_name="individual.education.lines", inverse_name="individual_id", string="", required=False, )

class individualeducationlines(models.Model):
    _name = 'individual.education.lines'

    response_id = fields.Many2one(comodel_name="res.users", string="Name", required=True, )
    position_id = fields.Selection(selection=[('parent', 'Parent'), ('supervisor', 'Supervisor'),('medical', 'Medical User'),('psychological', 'Psychological User'),('physiotherapy', 'Physiotherapy User'),('occupational', 'Occupational User'),('speech', 'Speech User'),('special', 'Special Education User'),('esocial','E-social User')], string='Position', )
    individual_id = fields.Many2one(comodel_name="individual.education")