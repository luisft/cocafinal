import web
import config

db = config.db


def get_all_pedidos():
    try:
        return db.select('pedidos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_pedidos(id_pedido):
    try:
        return db.select('pedidos', where='id_pedido=$id_pedido', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_pedidos(id_pedido):
    try:
        return db.delete('pedidos', where='id_pedido=$id_pedido', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_pedidos(producto,presentacion,cantidad,precio):
    try:
        return db.insert('pedidos',producto=producto,
presentacion=presentacion,
cantidad=cantidad,
precio=precio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_pedidos(id_pedido,producto,presentacion,cantidad,precio):
    try:
        return db.update('pedidos',id_pedido=id_pedido,
producto=producto,
presentacion=presentacion,
cantidad=cantidad,
precio=precio,
                  where='id_pedido=$id_pedido',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
