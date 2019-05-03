from odoo import models, fields, api, _


class accrGenerateNutritionStudents(models.TransientModel):
    _name = "accr.generate.nutrition.students"
    _description = "Generate Nutrition Students"


    students = fields.Many2many('x_student', 'generate_get_students_rel', 'generate_id', 'student_id',  required=True, string=u"Students" )

    @api.multi
    def act_gen_nutrition_students(self):
        for record in self:
            students = []
            for student in record.students:
                students.append({'student': student.id})
            self.env['accr.nutrition.student'].create(students)
            return {'type': 'ir.actions.act_window_close'}
