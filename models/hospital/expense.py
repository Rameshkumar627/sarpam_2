# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Expense(models.Model):
    _name = 'hospital.expense'

    name = fields.Char(string='Sequence', readonly=True)
    partner_id = fields.Many2one(comodel_name='partner.partner', string='Partner', required=True)
    partner_uid = fields.Char(string='Partner ID', related='partner_id.partner_uid')
    date = fields.Date(string='Date', required=True)
    total = fields.Float(string='Total', readonly=True)
    expense_detail_ids = fields.One2many(comodel_name='hospital.expense.detail',
                                         inverse_name='expense_id',
                                         string='Expense Details')
    state = fields.Selection([('draft', 'Draft'), ('paid', 'Paid')],
                             default='draft',
                             string='State')
    comment = fields.Text(string='Comment')


Expense()


class ExpenseDetail(models.Model):
    _name = 'hospital.expense.detail'

    name = fields.Char(string='Description', required=True)
    amount = fields.Float(string='Amount', required=True)
    expense_id = fields.Many2one(comodel_name='hospital.expense', string='Expense')


ExpenseDetail()



