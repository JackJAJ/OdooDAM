# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectoDam(http.Controller):
#     @http.route('/proyecto_dam/proyecto_dam', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_dam/proyecto_dam/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_dam.listing', {
#             'root': '/proyecto_dam/proyecto_dam',
#             'objects': http.request.env['proyecto_dam.proyecto_dam'].search([]),
#         })

#     @http.route('/proyecto_dam/proyecto_dam/objects/<model("proyecto_dam.proyecto_dam"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_dam.object', {
#             'object': obj
#         })
