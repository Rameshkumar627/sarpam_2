# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Admission(models.Model):
    _name = 'ipt.admission'

    sequence = fields.Char(string='Sequences')
    date = fields.Date(string='Date')

    # patient Details
    patient_id = fields.Many2one(comodel_name='patient.patient', string='Patient')
    patient_uid = fields.Char(string='Patient ID', related='patient_id.patient_uid')
    patient_contact = fields.Char(string='Patient Contact')
    patient_type = fields.Many2one(comodel_name='patient.type', string='Type')
    relatives_id = fields.Many2one(comodel_name='human.contact', string='Admission Contact')
    relatives_contact = fields.Char(string='Phone', related='relatives_id.phone')
    reason = fields.Many2one(comodel_name='patient.admission.reason', string='Reason')
    comment = fields.Text(string='Comment')

    # Status
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('cancelled', 'Cancelled')],
                             string='State')

    # Documents
    attachment_ids = fields.One2many(comodel_name='patient.attachment',
                                     inverse_name='admission_id',
                                     string='Attachment')


Admission()


