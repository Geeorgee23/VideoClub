# -*- coding: utf-8 -*-
# from odoo import http


# class VideoclubApp(http.Controller):
#     @http.route('/videoclub_app/videoclub_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/videoclub_app/videoclub_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('videoclub_app.listing', {
#             'root': '/videoclub_app/videoclub_app',
#             'objects': http.request.env['videoclub_app.videoclub_app'].search([]),
#         })

#     @http.route('/videoclub_app/videoclub_app/objects/<model("videoclub_app.videoclub_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('videoclub_app.object', {
#             'object': obj
#         })
