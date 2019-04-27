from odoo import models, fields, api,  _

class accrMedicineFoodIntolerance(models.Model):

    _name = "accr.medicine.food.Intolerance"
    _description = "ACCR Medicine Food Intolerance"

    name = fields.Char(string=u'Name')