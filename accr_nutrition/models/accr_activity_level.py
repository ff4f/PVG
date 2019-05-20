from odoo import models, fields

class accrActivityLevel(models.Model):
    _name = 'accr.activity.level'

    name = fields.Char(string=u"Activity.Level", required=True)