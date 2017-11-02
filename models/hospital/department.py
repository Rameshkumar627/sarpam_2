# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Department(models.Model):
    _name = 'hospital.department'

    name = fields.Char(string='Department')
    incharge_id = fields.Many2one(comodel_name='employee.employee', string='Incharge')
    comment = fields.Text(string='Comment')


Department()

