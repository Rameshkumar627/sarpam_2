# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class IptRemainder(models.Model):
    _name = 'ipt.remainder'

    date = fields.Datetime(string='Date')
    reminder = fields.Text(string='Reminder')
    reminder_to = fields.Many2one(comodel_name='employee.employee', string='Reminder To')
    reminder_mode = fields.Selection([('sms', 'SMS'), ('email', 'EMail')], string='Mode')
    comment = fields.Text(string='Comment')

    ipt_id = fields.Many2one(comodel_name='ipt.form', string='IPT')


IptRemainder()
