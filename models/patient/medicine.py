# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class PatientMedicine(models.Model):
    _name = 'patient.medicine'

    sequence = fields.Char(string='Sequence')
    date = fields.Datetime(string='Date')

    patient_id = fields.Many2one(comodel_name='patient.patient', string='Patient')
    patient_uid = fields.Char(string='Patient ID', related='patient_id.patient_uid')
    patient_contact = fields.Char(string='Patient Contact')

    medicine_lines = fields.One2many(comodel_name='patient.medicine.detail',
                                     inverse_name='patient_medicine_id',
                                     string='Medicine')

    opt_id = fields.Many2one(comodel_name='opt.form', string='OPT')
    ipt_id = fields.Many2one(comodel_name='ipt.form', string='IPT')

    comment = fields.Text(string='Comment')


PatientMedicine()


class PatientMedicineDetail(models.Model):
    _name = 'patient.medicine.detail'

    medicine = fields.Many2one(comodel_name='product.product')
    days = fields.Integer(string='Days')
    fore_noon = fields.Boolean(string='Fore Noon')
    noon = fields.Boolean(string='Noon')
    after_noon = fields.Boolean(string='After Noon')

    patient_medicine_id = fields.Many2one(comodel_name='patient.medicine', string='Medicine')


PatientMedicine()
