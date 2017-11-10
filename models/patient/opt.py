# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class OPT(models.Model):
    _name = 'opt.form'

    sequence = fields.Char(string='Sequence')
    date = fields.Datetime(string='Date')

    patient_id = fields.Many2one(comodel_name='patient.patient', string='Patient')
    patient_uid = fields.Char(string='Patient ID', related='patient_id.patient_uid')
    patient_contact = fields.Char(string='Patient Contact')
    symptoms_ids = fields.Many2many(comodel_name='patient.opt.symptoms', string='Symptoms')
    diagnosis_ids = fields.Many2many(comodel_name='patient.opt.diagnosis', string='Diagnosis')
    scan_ids = fields.Many2many(comodel_name='lab.scan', string='Scan')
    test_ids = fields.Many2many(comodel_name='lab.test', string='Test')
    medicine_ids = fields.One2many(comodel_name='patient.medicine',
                                   inverse_name='opt_id',
                                   string='Medicine')
    comment = fields.Text(string='Comment')
    report = fields.Html(string='Report')

    # Status
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('cancelled', 'Cancelled')],
                             string='State')

    # Documents
    attachment_ids = fields.One2many(comodel_name='patient.attachment',
                                     inverse_name='opt_id',
                                     string='Attachment')


OPT()
