# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class Product(models.Model):
    _name = 'product.product'
    _description = 'Product'
    _order = 'name'

    # Product
    name = fields.Char(string='Name', required=True)
    specification = fields.Text(string='Specification')
    product_group = fields.Many2one(comodel_name='product.groups', ondelete='cascade',
                                    required=True, string='Group')
    product_sub_group = fields.Many2one(comodel_name='product.subgroups', ondelete='cascade',
                                        required=True, string='Sub Group')
    average_price = fields.Float(string='Average Price',
                                 invisible="[('classification', '=', True)]")
    classification = fields.Boolean(string='Classify')
    uom = fields.Many2one(comodel_name='product.uom', ondelete='cascade',
                          required=True, string='UOM')

    parent_id = fields.Many2one(comodel_name='product.product', ondelete='cascade',
                                string='Sub-Product Of')
    child_ids = fields.One2many(comodel_name='product.product',
                                inverse_name='parent_id',
                                string='Product')
    hsn_code = fields.Char(string='HSN Code')
    code = fields.Char(string='Product Code')
    stock_ids = fields.One2many(comodel_name='stock.stock',
                                inverse_name='product_id',
                                string='Stock')
    comments = fields.Text(string='Comments')

    sale_price_ids = fields.One2many(comodel_name='product.sale.price',
                                     inverse_name='product_id',
                                     string='Sale Price')
    purchase_price_ids = fields.One2many(comodel_name='product.purchase.price',
                                         inverse_name='product_id',
                                         string='Purchase Price')


Product()





