# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Ward(models.Model):
    _name = 'hospital.ward'

    name = fields.Char(string='Ward', required=True)
    incharge_id = fields.Many2one(comodel_name='employee.employee', string='Incharge')
    comment = fields.Text(string='Comment')


Ward()


class Bed(models.Model):
    _name = 'hospital.bed'

    name = fields.Char(string='Bed', required=True)
    ward_id = fields.Many2one(comodel_name='hospital.ward', string='Ward')
    comment = fields.Text(string='Comment')


Bed()
