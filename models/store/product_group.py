# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class ProductGroup(models.Model):
    _name = 'product.group'
    _description = 'Product Group'

    name = fields.Char(string='Group', required=True)
    code = fields.Char(string='Group Code', required=True)
    active = fields.Boolean(string='Active', default=True)


ProductGroup()
