# -*- coding: utf-8 -*-

from odoo import models, fields, api


class usuario(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
    _description = 'Modelo para gestionar usuarios'

    premium = fields.Boolean( string = 'Premium', default = False )
    karma = fields.Integer( string = 'Karma', default = 0 )


    @api.model
    def modify_user(self, username, premium, karma):
        """Método para modificar el estado premium y el karma del usuario."""
        user = self.env['app.usuario'].search([('name', '=', username)])
        if user:
            user.write({'premium': premium, 'karma': karma})
            return True
        else:
            return False

    @api.model
    def get_user_info(self, username):
        """Método para obtener información del usuario."""
        user = self.env['app.usuario'].search([('name', '=', username)])
        if user:
            return {'premium': user.premium, 'karma': user.karma}
        else:
            return {}
