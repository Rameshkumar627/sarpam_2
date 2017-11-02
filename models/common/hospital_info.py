# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


# Hospital Information
class BloodGroup(models.Model):
    _name = 'blood.group'

    name = fields.Char(string='Blood Group')


BloodGroup()


class HospitalLocation(models.Model):
    _name = 'hospital.location'

    name = fields.Char(string='Hospital Location')


HospitalLocation()


class StockLocation(models.Model):
    _name = 'stock.location'

    name = fields.Char(string='Stock Location')


StockLocation()

