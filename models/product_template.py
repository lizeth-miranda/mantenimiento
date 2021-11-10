# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, _


class promaint(models.Model):
    _inherit = 'product.template'

    # enviar = fields.Selection([
    #     ('crear', 'Crear en Mantenimiento'), ], string="Enviar",)

    # @api.model
    # def create(self, vals_list):
    #     res = super(promaint, self).create(vals_list)
    #     if self.enviar in ['crear', 'Crear en Mantenimiento']:
    #         print("funciona")
    #         vals = {
    #             'name': res.name,
    #             'serial_no': res.num_serie,
    #         }
    #         self.env['maintenance.equipment'].create(vals)

    #     return res
    marca = fields.Char(string="Marca",)
    modelo = fields.Char(string="Modelo",)
    proveedor = fields.Many2one(
        string="Proveedor", comodel_name="res.partner",)

    def enviar(self):
        for record in self:
            vals = {
                'name': record.name,
                'serial_no': record.num_serie,
                'model': record.modelo,
                'marca': record.marca,
                'partner_id': record.proveedor.id,
                'cost': record.standard_price,
            }
            record.env['maintenance.equipment'].create(vals)
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Registro Exitoso',
                    'type': 'rainbow_man',
                }
            }
