import json
import random
import urllib.request
import getpass  # Módulo para manejar contraseñas de manera más segura

HOST = 'localhost'
PORT = 8069
DB = 'ProyectoDAM'
USER = 'DIJ'
PASS = getpass.getpass(prompt='Contraseña de Odoo: ')  # Solicita la contraseña de Odoo de forma segura

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type": "application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

# Registro de Ventas y Facturación

def create_sale_order(url, partner_id, product_id, quantity):
    uid = json_rpc(url, "common", "login", DB, USER, PASS)
    sale_order_vals = {
        'partner_id': partner_id,
        'order_line': [(0, 0, {
            'product_id': product_id,
            'product_uom_qty': quantity,
        })],
    }
    sale_order_id = json_rpc(url, "object", "execute", DB, uid, PASS, 'sale.order', 'create', sale_order_vals)
    return sale_order_id

def generate_invoice(url, sale_order_id):
    uid = json_rpc(url, "common", "login", DB, USER, PASS)
    invoice_id = json_rpc(url, "object", "execute", DB, uid, PASS, 'sale.order', 'action_invoice_create', [sale_order_id])
    return invoice_id

def generate_invoice_pdf(url, invoice_id):
    uid = json_rpc(url, "common", "login", DB, USER, PASS)
    pdf_data = json_rpc(url, "report", "get_pdf", DB, uid, PASS, invoice_id, 'account.report_invoice')
    # Handle PDF data as needed
    return pdf_data

# Creación de Usuarios/Clientes y Cambio de Contraseña:

def create_user(url, username, password):
    params = {
        "name": username,
        "login": username,
        "password": password,
    }
    uid = json_rpc(url, "common", "login", DB, USER, PASS)
    partner_id = json_rpc(url, "object", "execute", DB, uid, PASS, 'res.partner', 'create', params)
    return partner_id

def change_password(url, username, new_password):
    uid = json_rpc(url, "common", "login", DB, USER, PASS)
    user_id = json_rpc(url, "object", "execute", DB, uid, PASS, 'res.users', 'search', [('login', '=', username)])
    if user_id:
        json_rpc(url, "object", "execute", DB, uid, PASS, 'res.users', 'write', user_id, {'password': new_password})
        return True
    return False

# Funciones adicionales para mejorar la claridad del código

def authenticate_odoo():
    url = f"http://{HOST}:{PORT}/jsonrpc"
    uid = json_rpc(url, "common", "login", DB, USER, PASS)
    return url, uid

def print_authentication_status(uid):
    if uid:
        print(f"Autenticación exitosa. ID de usuario: {uid}")
    else:
        print("Falló la autenticación.")

def main():
    url, uid = authenticate_odoo()
    print_authentication_status(uid)

    if uid:
        # Ejemplo: Obtener datos del usuario
        user_data = json_rpc(url, "object", "execute", DB, uid, PASS, 'res.users', 'read', [uid], {'fields': ['name', 'email']})
        print("Datos del usuario:", user_data)

        # Ejemplo: Verificar estado premium
        premium_status = json_rpc(url, "object", "execute", DB, uid, PASS, 'res.users', 'read', [uid], {'fields': ['is_premium']})
        print("Estado premium:", premium_status[0]['is_premium'])

        # Ejemplo: Obtener karma del usuario
        user_karma = json_rpc(url, "object", "execute", DB, uid, PASS, 'res.users', 'read', [uid], {'fields': ['karma']})
        print("Karma del usuario:", user_karma[0]['karma'])

if __name__ == "__main__":
    main()
