# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class Tax(models.Model):
    _name = 'product.tax'
    _description = 'Tax'
    _order = 'name'

    name = fields.Char(string='Tax', required=True)
    rate = fields.Float(string='Rate (%)', required=True)


Tax()
