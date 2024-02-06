# -*- coding: utf-8 -*-

from odoo import models, fields, api


class res_partner(models.Model):
    _name = 'proyecto_dam.res_partner'
    _description = 'Informació del Karma per a l\'usuari'

    _inherit = 'res.partner'

    karma = fields.Integer(string='Karma')