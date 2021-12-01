# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class promaint(models.Model):
    _inherit = 'product.template'

    marca = fields.Char(string="Marca",)
    modelo = fields.Char(string="Modelo",)
    proveedor = fields.Many2one(
        string="Proveedor", comodel_name="res.partner",)

    def enviar(self):
        for record in self:
            buscar = self.env['maintenance.equipment'].search_count([
                ('serial_no', '=', record.num_serie),
            ])
            if buscar > 0:
                raise ValidationError(
                    _("Uno o varios de los registros ya existen"))

            elif not buscar:
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
