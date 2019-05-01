import datetime
from odoo import models, fields, api, _


class accrStudentNutritionDetails(models.Model):
    _name = "accr.student.nutrition.details"
    _description = "Student Nutrition Details"

    student = fields.Many2one('x_student', string=u'Student', required=True, )
    name = fields.Char(compute='_compute_name', string=u'Name', readonly=True, )
    age = fields.Char(related='student.x_studio_age', string=u"Age", readonly=True, store=False, )
    diagnosis = fields.Text(related='student.x_studio_diagnosis', string=u'Diagnosis', readonly=True, store=False, )
    residential_section = fields.Many2one(related='student.x_studio_residential_sections', string=u'Residential Section', readonly=True, store=False, )
    food_preferences = fields.One2many('accr.student.food.preferences', 'nutrition_details', string=u'Food Preferences', )
    food_intolerance = fields.One2many('accr.student.food.intolerance', 'nutrition_details', string=u'Food Intolerance', compute='_compute_medications_intolerance' )
    medications = fields.One2many(related='student.x_medications', string=u'Medications', store=False)
    height = fields.Integer(string=u'Height', required=True, )
    weight = fields.Integer(string=u'Weight', required=True, )
    diet = fields.Many2one('accr.diet', string=u'Diet', required=True, )
    requirements = fields.Many2one('accr.nutrition.requirements', string=u'Requirements', )
    physical_activity = fields.Many2one('accr.physical.activity', string=u'Physical Activity', )
    water_intake = fields.Many2one('accr.water.intake', string=u'Water Intake', )
    nutritional_needs = fields.Many2one('accr.nutritional.needs', string=u'Nutritional Needs', )

    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - '+ record.create_date.strftime("%Y-%m-%d")


    @api.multi
    @api.depends('medications')
    def _compute_medications_intolerance(self):
        for record in self:
            food_types = []
            current_date = datetime.datetime.now()
            for medication in record.medications:
                if current_date > medication.end_date_time:
                    medicine = medication.medicine
                    for medical_contraindication in medicine.medical_contraindication:
                        for food_type in medical_contraindication.food_types:
                            food_types.append({'student': record.student.id, 'nutrition_details': record.id, 'food_type':food_type.id})
            
            record.food_intolerance = self.env['accr.student.food.intolerance'].create(food_types)