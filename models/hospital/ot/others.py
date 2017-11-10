# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class OperationType(models.Model):
    _name = 'hospital.ot.type'

    name = fields.Char(string='Type', required=True)
    comment = fields.Text(string='Comment')


OperationType()


