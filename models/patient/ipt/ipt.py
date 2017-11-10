# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class IPT(models.Model):
    _name = 'ipt.form'

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

    # Treatment
    treatment_ids = fields.One2many(comodel_name='ipt.treatment',
                                    inverse_name='ipt_id',
                                    string='Treatment')
    reminder_ids = fields.One2many(comodel_name='ipt.remainder',
                                   inverse_name='ipt_id',
                                   string='Reminder')
    doctor_visit_ids = fields.One2many(comodel_name='ipt.doctor.visit',
                                       inverse_name='ipt_id',
                                       string='Doctor Visit')
    medicine_ids = fields.One2many(comodel_name='patient.medicine',
                                   inverse_name='ipt_id',
                                   string='Medicine')
    hospitality_ids = fields.One2many(comodel_name='ipt.hospitality',
                                      inverse_name='ipt_id',
                                      string='Hospitality')

    report = fields.Html(string='Report')

    # Status
    state = fields.Selection([('open', 'Draft'),
                              ('closed', 'Closed')],
                             string='State')

    # Documents
    attachment_ids = fields.One2many(comodel_name='patient.attachment',
                                     inverse_name='ipt_id',
                                     string='Attachment')


IPT()




