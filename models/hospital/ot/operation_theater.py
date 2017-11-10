# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class OperationTheater(models.Model):
    _name = 'hospital.ot'

    sequence = ''
    patient_id = ''
    patient_uid = ''
    from_date = ''
    till_date = ''
    type = ''
    operation = ''
    staff_ids = ''
    attachment_ids = ''
    comment = ''


OperationTheater()


class OperationTheaterEmployee(models.Model):
    _name = 'hospital.ot.employee'

    employee_id = ''
    employee_uid = ''


OperationTheaterEmployee()






