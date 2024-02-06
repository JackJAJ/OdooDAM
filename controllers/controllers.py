# -*- coding: utf-8 -*-
from odoo import http
import json

class OdooJSONController(http.Controller):

    @http.route('/jsonrpc/authenticate', type='json', auth='none', methods=['POST'], csrf=False)
    def authenticate(self, **params):
        username = params.get('username')
        password = params.get('password')

        if username == "admin" and password == "admin":
            return {"result": "Authentication successful"}
        else:
            return {"error": "Authentication failed"}


    @http.route('/jsonrpc/modify_user', type='json', auth='none', methods=['POST'], csrf=False)
    def modify_user(self, **params):
        username = params.get('username')
        premium = params.get('premium')
        karma = params.get('karma')
        
        return {"result": f"User {username} modified. Premium: {premium}, Karma: {karma}"}

    @http.route('/jsonrpc/get_user_info', type='json', auth='none', methods=['POST'], csrf=False)
    def get_user_info(self, **params):
        username = params.get('username')
        
        return {"premium": True, "karma": 100}
