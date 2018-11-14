# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models,fields,api

class website_portfolio(models.Model):
    _name="website.portfolio"
    _description = "Website Portfolio"    
    
    category_id=fields.Many2one("website.portfolio.category",string="Category", required=False)
    img=fields.Binary(string="Image",help="preffered size 300x300")
    name=fields.Char(string="Title",required=False)
    desc=fields.Text(string="Description")
    is_active=fields.Boolean(string="Active",default=True)
    website_id = fields.Many2one("website", related="category_id.website_id", required=True, readonly = False)       
    
    
