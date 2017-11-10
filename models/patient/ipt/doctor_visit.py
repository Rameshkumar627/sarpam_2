# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class IptDoctorVisit(models.Model):
    _name = 'ipt.doctor.visit'

    date = fields.Datetime(string='Date')
    comment = fields.Text(string='Comment')

    ipt_id = fields.Many2one(comodel_name='ipt.form', string='IPT')


IptDoctorVisit()
