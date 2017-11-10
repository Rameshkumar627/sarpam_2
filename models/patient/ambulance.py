# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Ambulance(models.Model):
    _name = 'ipt.ambulance'

    sequence = fields.Char(string='Sequence')
    date = fields.Datetime(string='Date')

    # Patient Details
    patient_id = fields.Many2one(comodel_name='patient.patient', string='Patient')
    patient_uid = fields.Char(string='Patient ID', related='patient_id.patient_uid')
    patient_contact = fields.Char(string='Patient Contact')
    patient_type = fields.Many2one(comodel_name='patient.type', string='Type')
    relatives_id = fields.Many2one(comodel_name='human.contact', string='Admission Contact')
    relatives_contact = fields.Char(string='Phone', related='relatives_id.phone')

    # Service Details
    from_place = fields.Char(string='From Place')
    till_place = fields.Char(string='Till Place')
    distance = fields.Float(string='Distance (KM)')
    reason = fields.Many2one(comodel_name='patient.admission.reason', string='Reason')
    driver_id = fields.Many2one(comodel_name='employee.employee', string='Driver')
    driver_contact = fields.Char(string='Driver Contact')
    staff_ids = fields.Many2many(comodel_name='employee.employee', string='Staff')
    comment = fields.Text(string='Comment')

    # Status
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('cancelled', 'Cancelled')],
                             string='State')

    # Documents
    attachment_ids = fields.One2many(comodel_name='patient.attachment',
                                     inverse_name='ambulance_id',
                                     string='Attachment')


Ambulance()

