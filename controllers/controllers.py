# -*- coding: utf-8 -*-
from odoo import http

# class KitchenOrders(http.Controller):
#     @http.route('/kitchen_orders/kitchen_orders/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kitchen_orders/kitchen_orders/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kitchen_orders.listing', {
#             'root': '/kitchen_orders/kitchen_orders',
#             'objects': http.request.env['kitchen_orders.kitchen_orders'].search([]),
#         })

#     @http.route('/kitchen_orders/kitchen_orders/objects/<model("kitchen_orders.kitchen_orders"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kitchen_orders.object', {
#             'object': obj
#         })