# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Ordenes de Cocina",
  "summary"              :  "Crear Ordenes de Cocina.",
  "category"             :  "Point Of Sale",
  "version"              :  "1.0.1",
  "author"               :  "VK&C.",
  "license"              :  "Other proprietary",
  "website"              :  "vkyc11.odoo.com",
  "description"          :  """Modulo para la creacion de ordenes de cocina""",
  "depends"              :  [
                             'point_of_sale',
                             'sale',
                             'mrp',
                             'stock',
                            ],
  "data"                 :  [
                              'views/pos_to_sales_order_view.xml',
                              'views/templates.xml',
                              'views/kitchen_orders.xml',
                              'views/product_view.xml',
                              'data/pos_to_sale_order_demo.xml',
                              'security/ir.model.access.csv',
                              # 'views/pos_ticket_view.xml',
                            ],
  "qweb"                 :  [
                              'static/src/xml/pos_to_sale_order.xml',
                              'static/src/xml/pos_ticket_view.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
}