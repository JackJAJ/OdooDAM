# -*- coding: utf-8 -*-

from odoo import models, fields, api

class usuario(models.Model):
    
    _name = 'proyecto_dam.usuario'
    _description = 'Modelo para gestionar usuarios'

    id = fields.Integer
    name = fields.Char(string='Nombre de usuario', required=True)
    password = fields.Char(string='Contraseña', required=True)
    confirm_password = fields.Char(string='Confirmar Contraseña', required=True)
    premium = fields.Boolean(string='Premium', default=False)
    karma = fields.Integer(string='Karma', default=0)

    @api.constrains('password', 'confirm_password')
    def _check_passwords_match(self):
        for record in self:
            if record.password != record.confirm_password:
                raise ValidationError("Las contraseñas no coinciden.")

    @api.model
    def authenticate_user(self, username, password):
        """Método para autenticar al usuario."""
        user = self.env['app.usuario'].search([('name', '=', username), ('password', '=', password)])
        if user:
            return True
        else:
            return False

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
