# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class IptTreatment(models.Model):
    _name = 'ipt.treatment'

    from_time = fields.Datetime(string='From')
    till_time = fields.Datetime(string='Till')
    total_hours = fields.Float(string='Total Hrs')
    amount = fields.Float(string='Amount')
    treatment_id = fields.Many2one(comodel_name='treatment.treatment', string='Treatment')
    comment = fields.Text(string='Comment')

    ipt_id = fields.Many2one(comodel_name='ipt.form', string='IPT')


IptTreatment()


class Treatment(models.Model):
    _name = 'treatment.treatment'

    treatment = fields.Char(string='Treatment')
    cost = fields.Float(string='Cost')


Treatment()
