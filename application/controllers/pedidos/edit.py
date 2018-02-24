import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_pedido, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_pedido) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                return self.GET_EDIT(id_pedido) # call GET_EDIT function
               # raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_pedido, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_pedido) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                return self.POST_EDIT(id_pedido) # call POST_EDIT function
                #raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_pedido, **k):
        message = None # Error message
        id_pedido = config.check_secure_val(str(id_pedido)) # HMAC id_pedido validate
        result = config.model.get_pedidos(int(id_pedido)) # search for the id_pedido
        result.id_pedido = config.make_secure_val(str(result.id_pedido)) # apply HMAC for id_pedido
        return config.render.edit(result, message) # render pedidos edit.html

    @staticmethod
    def POST_EDIT(id_pedido, **k):
        form = config.web.input()  # get form data
        form['id_pedido'] = config.check_secure_val(str(form['id_pedido'])) # HMAC id_pedido validate
        # edit user with new data
        result = config.model.edit_pedidos(
            form['id_pedido'],form['producto'],form['presentacion'],form['cantidad'],form['precio'],
        )
        if result == None: # Error on udpate data
            id_pedido = config.check_secure_val(str(id_pedido)) # validate HMAC id_pedido
            result = config.model.get_pedidos(int(id_pedido)) # search for id_pedido data
            result.id_pedido = config.make_secure_val(str(result.id_pedido)) # apply HMAC to id_pedido
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/pedidos') # render pedidos index.html
