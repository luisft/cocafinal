import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_pedido, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_pedido) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                #raise config.web.seeother('/guess') # render guess.html
                return self.GET_DELETE(id_pedido) # call GET_DELETE function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_pedido, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_pedido) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                 return self.POST_DELETE(id_pedido) # call POST_DELETE function
                #raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_pedido, **k):
        message = None # Error message
        id_pedido = config.check_secure_val(str(id_pedido)) # HMAC id_pedido validate
        result = config.model.get_pedidos(int(id_pedido)) # search  id_pedido
        result.id_pedido = config.make_secure_val(str(result.id_pedido)) # apply HMAC for id_pedido
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_pedido, **k):
        form = config.web.input() # get form data
        form['id_pedido'] = config.check_secure_val(str(form['id_pedido'])) # HMAC id_pedido validate
        result = config.model.delete_pedidos(form['id_pedido']) # get pedidos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_pedido = config.check_secure_val(str(id_pedido))  # HMAC user validate
            id_pedido = config.check_secure_val(str(id_pedido))  # HMAC user validate
            result = config.model.get_pedidos(int(id_pedido)) # get id_pedido data
            result.id_pedido = config.make_secure_val(str(result.id_pedido)) # apply HMAC to id_pedido
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/pedidos') # render pedidos delete.html 
