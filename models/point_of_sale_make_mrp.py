# -*- coding: utf-8 -*-

##############################################################################
#                                                                           ##
#       abiezersifontes@gmail.com                                           ##
#                                                                           ##
##############################################################################

from odoo import models, fields, api
from odoo.exceptions import Warning


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def create_mrp_from_pos(self, products):
        product_ids = []
        print ("products", products)
        if products:
            for product in products:
                flag = 1
                if product_ids:
                    for product_id in product_ids:
                        if product_id['id'] == product['id']:
                            product_id['qty'] += product['qty']
                            flag = 0
                if flag:
                    product_ids.append(product)
            for prod in product_ids:
                if prod['qty'] > 0:
                    product = self.env['product.product'].search([('id', '=', prod['id'])])
                    bom_count = self.env['mrp.bom'].search([('product_tmpl_id', '=', prod['product_tmpl_id'])])
                    if bom_count:
                        bom_temp = self.env['mrp.bom'].search([('product_tmpl_id', '=', prod['product_tmpl_id']),
                                                               ('product_id', '=', False)])
                        bom_prod = self.env['mrp.bom'].search([('product_id', '=', prod['id'])])
                        if bom_prod:
                            bom = bom_prod[0]
                        elif bom_temp:
                            bom = bom_temp[0]
                        else:
                            bom = []
                            print ("This product variants have no exact BOM")
                        if bom:
                            vals = {
                                'origin': 'POS-' + prod['pos_reference'],
                                'state': 'confirmed',
                                'product_id': prod['id'],
                                'product_tmpl_id': prod['product_tmpl_id'],
                                'product_uom_id': prod['uom_id'],
                                'product_qty': prod['qty'],
                                'bom_id': bom.id,
                            }
                            self.sudo().create(vals)
        return True        
    
    # @api.multi
    # def finish_kitchen_order(self):
    #     return open_produce_product(self)
        
        


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    to_make_mrp = fields.Boolean(string='Crear Orden de Produccion',
                                 help="Verifique si el producto amerita una orden de produccion")

    @api.onchange('to_make_mrp')
    def onchange_to_make_mrp(self):
        if self.to_make_mrp:
            if not self.bom_count:
                raise Warning('Por favor seleccione una lista de materiales para este produccto.')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.onchange('to_make_mrp')
    def onchange_to_make_mrp(self):
        if self.to_make_mrp:
            if not self.bom_count:
                raise Warning('Por favor seleccione una lista de Materiales Para Este Producto.')

    def is_to_make_mrp(id):
        if(id==8):
            return True
        else:
            return id