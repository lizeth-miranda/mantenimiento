# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, _


class mainten(models.Model):
    _inherit = 'maintenance.equipment'

    marca = fields.Char(string="Marca",)
    obra = fields.Many2one(
        comodel_name='account.analytic.account', string="Obra", )
    sistemas = fields.Boolean(string='Sistemas', default=False,)
