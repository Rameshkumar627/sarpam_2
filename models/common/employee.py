# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Employee(models.Model):

    _name = 'employee.employee'
    _inherit = 'msg.msg'
    _inherits = {"patient.patient": "source_id"}

    # Official Information
    source_id = fields.Many2one(comodel_name='patient.patient', string='Source')
    image = fields.Binary(string='Image')
    position = fields.Char(string='Job Position')
    name = fields.Char(string='Employee Name', required=True)
    is_doctor = fields.Boolean(string='Is Doctor')
    employee_uid = fields.Char(string='Employee ID')
    employee_type_id = fields.Many2one(comodel_name='employee.type', string='Employee Type', required=True)
    date_of_join = fields.Date(string='Date Of Joining')
    date_of_exit = fields.Date(string='Date Of Exit')
    phone_primary = fields.Char(string='Phone Primary')
    phone_secondary = fields.Char(string='Phone Secondary')
    email = fields.Char(string='Email', required=True)
    pan = fields.Char(string='PAN', required=True)
    aadhar_card = fields.Char(string='Aadhar Card')
    bank_name = fields.Many2one(comodel_name='account.bank', string='Bank')
    account_no = fields.Char(string='Bank Account No')
    direct_reportee_id = fields.Many2one(comodel_name='employee.employee', string='Direct Reportee', index=True)
    subordinate_ids = fields.One2many(comodel_name='employee.employee',
                                      inverse_name='direct_reportee_id',
                                      string='Subordinates')
    active = fields.Boolean(string='Acive', default=True)

    # Medical Information
    allergic_towards = fields.Char(string='Allergic Towards')
    blood_group = fields.Many2one(comodel_name='human.blood.group', string='Blood Group')
    medical_insurance = fields.Char(string='Medical Insurance')

    # Personal Information
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Integer(string='Age', readonly=True)
    sex = fields.Selection([('male', 'Male'),
                            ('female', 'Female'),
                            ('transgender', 'Transgender')],
                           string='Sex')
    marital_status = fields.Selection([('married', 'married'),
                                       ('unmarried', 'Unmarried'),
                                       ('divorced', 'Divorced')],
                                      string='Marital Status')

    contact_address = fields.One2many(comodel_name='human.contact',
                                      inverse_name='hospital_employee_id',
                                      string='Contact Address')
    emergency_contact = fields.Many2one(comodel_name='human.contact', string='Emergency Contact')
    comments = fields.Text(string='Comments')

    # Professional Information
    education = fields.One2many(comodel_name='employee.education',
                                inverse_name='hospital_employee_id',
                                string='Education')
    experience = fields.One2many(comodel_name='employee.experience',
                                 inverse_name='hospital_employee_id',
                                 string='Experience')
    awards = fields.One2many(comodel_name='employee.awards',
                             inverse_name='hospital_employee_id',
                             string='Awards/Certification')

    # Programmatic
    status = fields.Selection([('draft', 'Draft'),
                               ('confirmed', 'Confirmed'),
                               ('exit', 'Exit')],
                              default='draft',
                              string='Status')

    # HR Information
    permission_approvar_id = fields.Many2one(comodel_name='employee.employee', string='Permission Approvar')
    leave_approvar_id = fields.Many2one(comodel_name='employee.employee', string='Leave Approvar')
    overtime_approvar_id = fields.Many2one(comodel_name='employee.employee', string='Overtime Approvar')

    @api.model
    def create(self, vals):
        k = super(Employee, self).create(vals)
        k.msg = "hi"
        k.msg_generation()
        return k


Employee()
