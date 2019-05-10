from odoo import models, fields

class accrFoodTextures(models.Model):
    _name = 'accr.food.textures'

    name = fields.Char(string=u'Food Textures', required=True, )