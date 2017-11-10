# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Deceased(models.Model):
    _name = 'ipt.deceased'

    date = fields.Date(string='Date')
    sequence = fields.Char(string='Sequence')

    # patient Details
    patient_id = fields.Many2one(comodel_name='patient.patient', string='Patient')
    patient_uid = fields.Char(string='Patient ID', related='patient_id.patient_uid')
    patient_contact = fields.Char(string='Patient Contact')
    patient_type = fields.Many2one(comodel_name='patient.type', string='Type')
    relatives_id = fields.Many2one(comodel_name='human.contact', string='Admission Contact')
    relatives_contact = fields.Char(string='Phone', related='relatives_id.phone')
    reason = fields.Many2one(comodel_name='patient.deceased.reason', string='Reason')

    # Hospital Details
    staff_ids = fields.Many2one(comodel_name='employee.employee', string='Doctor')
    comment = fields.Text(string='Comment')
    deceased_time = fields.Datetime(string='Deceased Time')
    attachment_ids = fields.One2many(comodel_name='patient.attachment',
                                     inverse_name='deceased_id',
                                     string='Attachment')

    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('cancelled', 'Cancelled')],
                             string='State')


Deceased()
