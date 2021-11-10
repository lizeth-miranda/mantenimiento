# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, _


class mainten(models.Model):
    _inherit = 'maintenance.equipment'

    marca = fields.Char(string="Marca",)
