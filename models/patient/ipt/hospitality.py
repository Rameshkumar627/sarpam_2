# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class IptHospitality(models.Model):
    _name = 'ipt.hospitality'

    from_time = fields.Datetime(string='From')
    till_time = fields.Datetime(string='Till')
    total_hours = fields.Float(string='Total Hrs')
    amount = fields.Float(string='Amount')
    bed_id = fields.Many2one(comodel_name='hospital.bed', string='Hospital Bed')
    comment = fields.Text(string='Comment')

    ipt_id = fields.Many2one(comodel_name='ipt.form', string='IPT')


IptHospitality()
