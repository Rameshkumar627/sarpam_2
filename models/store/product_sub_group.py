# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class ProductSubGroup(models.Model):
    _name = 'product.subgroup'
    _description = 'Product Sub-Group'

    name = fields.Char(string='Sub Group', required=True)
    code = fields.Char(string='Sub Group Code', required=True)
    active = fields.Boolean(string='Active', default=True)
    product_group = fields.Many2one(comodel_name='product.group', ondelete='cascade', string='Group', required=True)


ProductSubGroup()
