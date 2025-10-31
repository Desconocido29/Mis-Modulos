from odoo import models, fields, api

class Persona(models.Model):
    _name = 'persona.persona'
    _description = 'Persona'

    name = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    telefono_ids = fields.One2many(
        comodel_name='persona.telefono',
        inverse_name='persona_id',
        string='Teléfonos'
    )

    telefono_count = fields.Integer(
        string='Cantidad de teléfonos',
        compute='_compute_telefono_count'
    )

    @api.depends('telefono_ids')
    def _compute_telefono_count(self):
        for persona in self:
            persona.telefono_count = len(persona.telefono_ids)


class Telefono(models.Model):
    _name = 'persona.telefono'
    _description = 'Teléfono de la Persona'

    numero = fields.Char(string='Número de teléfono', required=True)
    tipo = fields.Selection([
        ('movil', 'Móvil'),
        ('casa', 'Casa'),
        ('trabajo', 'Trabajo'),
        ('otro', 'Otro'),
    ], string='Tipo', default='movil')
    fecha_registro = fields.Date(string='Fecha de registro', default=fields.Date.context_today)
    persona_id = fields.Many2one(
        comodel_name='persona.persona',
        string='Persona',
        ondelete='cascade'
    )
