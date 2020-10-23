# -*- coding: utf-8 -*-
from odoo import http

# class Newtask(http.Controller):
#     @http.route('/newtask/newtask/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/newtask/newtask/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('newtask.listing', {
#             'root': '/newtask/newtask',
#             'objects': http.request.env['newtask.newtask'].search([]),
#         })

#     @http.route('/newtask/newtask/objects/<model("newtask.newtask"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('newtask.object', {
#             'object': obj
#         })