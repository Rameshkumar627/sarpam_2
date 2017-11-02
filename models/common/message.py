# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Message(models.Model):
    _name = 'msg.msg'

    msg = fields.Char(string='Message')

    @api.multi
    def msg_generation(self, msg=None):
        print "ramesh"


Message()


