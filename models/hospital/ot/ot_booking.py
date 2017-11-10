# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class OperationBooking(models.Model):
    _name = 'hospital.ot.booking'

    from_date = fields.Datetime(string='From Date')
    till_date = fields.Datetime(string='Till Date')
    patient_id = fields.Many2one(comodel_name='patient.patient', string='Patient')
    patient_uid = fields.Char(string='Patient ID', related='patient_id.patient_uid')
    emergency_contact = fields.Char(string='Emergency Contact')
    relatives = ''
    type_id = fields.Many2one(comodel_name='hospital.ot.type', string='Type')
    advance_paid = fields.Float(string="Advance Paid")
    expected_amount = fields.Float(string="Amount")
    actual_amount = fields.Float(string="Actual Amount")
    staff_ids = fields.One2many(comodel_name='employee.employee')


OperationBooking()


class OperationBookingEmployee(models.Model):
    _name = 'hospital.ot.booking.employee'

    employee_id = fields.Many2one(comodel_name='employee.employee', string='Employee')
    employee_uid = fields.Char(string='Employee ID', related='employee_id.employee_uid')
    contact = fields.Char(string='Emergency Contact', related='')


OperationBookingEmployee()
