import web
import config
import json


class Api_pedidos:
    def get(self, id_pedido):
        try:
            # http://0.0.0.0:8080/api_pedidos?user_hash=12345&action=get
            if id_pedido is None:
                result = config.model.get_all_pedidos()
                pedidos_json = []
                for row in result:
                    tmp = dict(row)
                    pedidos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(pedidos_json)
            else:
                # http://0.0.0.0:8080/api_pedidos?user_hash=12345&action=get&id_pedido=1
                result = config.model.get_pedidos(int(id_pedido))
                pedidos_json = []
                pedidos_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(pedidos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            pedidos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pedidos_json)

# http://0.0.0.0:8080/api_pedidos?user_hash=12345&action=put&id_pedido=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, producto,presentacion,cantidad,precio):
        try:
            config.model.insert_pedidos(producto,presentacion,cantidad,precio)
            pedidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pedidos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_pedidos?user_hash=12345&action=delete&id_pedido=1
    def delete(self, id_pedido):
        try:
            config.model.delete_pedidos(id_pedido)
            pedidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pedidos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_pedidos?user_hash=12345&action=update&id_pedido=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_pedido, producto,presentacion,cantidad,precio):
        try:
            config.model.edit_pedidos(id_pedido,producto,presentacion,cantidad,precio)
            pedidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pedidos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            pedidos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pedidos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_pedido=None,
            producto=None,
            presentacion=None,
            cantidad=None,
            precio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_pedido=user_data.id_pedido
            producto=user_data.producto
            presentacion=user_data.presentacion
            cantidad=user_data.cantidad
            precio=user_data.precio
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_pedido)
                elif action == 'put':
                    return self.put(producto,presentacion,cantidad,precio)
                elif action == 'delete':
                    return self.delete(id_pedido)
                elif action == 'update':
                    return self.update(id_pedido, producto,presentacion,cantidad,precio)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
