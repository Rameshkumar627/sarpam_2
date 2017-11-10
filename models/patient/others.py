# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class PatientType(models.Model):
    '''Type namely emergency, casual'''
    _name = 'patient.type'

    type = fields.Char(string='Type')
    comment = fields.Text(string='Comment')


PatientType()


class PatientAttachment(models.Model):
    _name = 'patient.attachment'

    name = fields.Char(string='Name')
    files = fields.Binary(string='File')
    description = fields.Char(string='File Description')
    opt_id = fields.Many2one(comodel_name='opt.form', string='OPT')
    admission_id = fields.Many2one(comodel_name='ipt.admission', string='Admission')
    ambulance_id = fields.Many2one(comodel_name='ipt.ambulance', string='Ambulance')
    deceased_id = fields.Many2one(comodel_name='ipt.deceased', string='Deceased')
    ipt_id = fields.Many2one(comodel_name='ipt.form', string='IPT')


PatientAttachment()


class PatientAdmissionReason(models.Model):
    _name = 'patient.admission.reason'

    name = fields.Char(string='Name')


PatientAdmissionReason()


class OPTSymptoms(models.Model):
    _name = 'patient.opt.symptoms'

    name = fields.Char(string='Name')


PatientAdmissionReason()


class OPTDiagnosis(models.Model):
    _name = 'patient.opt.diagnosis'

    name = fields.Char(string='Name')


PatientAdmissionReason()


class LabScan(models.Model):
    _name = 'lab.scan'

    name = fields.Char(string='Scan')


LabScan()


class LabTest(models.Model):
    _name = 'lab.test'

    name = fields.Char(string='Test')


LabTest()


