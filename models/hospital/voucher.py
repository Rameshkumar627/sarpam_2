# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Voucher(models.Model):
    _name = 'hospital.voucher'

    name = fields.Char(string='Sequence', readonly=True)
    employee_id = fields.Many2one(comodel_name='employee.employee', string='Employee', required=True)
    employee_uid = fields.Char(string='Employee ID', related='employee_id.employee_uid')
    date = fields.Date(string='Date', required=True)
    total = fields.Float(string='Total', readonly=True)
    voucher_detail_ids = fields.One2many(comodel_name='hospital.voucher.detail',
                                         inverse_name='voucher_id',
                                         string='Voucher Details')
    state = fields.Selection([('draft', 'Draft'), ('paid', 'Paid')],
                             default='draft',
                             string='State')
    comment = fields.Text(string='Comment')


Voucher()


class VoucherDetail(models.Model):
    _name = 'hospital.voucher.detail'

    name = fields.Char(string='Description', required=True)
    amount = fields.Float(string='Amount', required=True)
    voucher_id = fields.Many2one(comodel_name='hospital.voucher', string='Voucher')


VoucherDetail()



