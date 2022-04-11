import web
import pyrebase
import firebase_config as token
import json  #incluir libreria JSON
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

urls = (
    '/', 'Index',
    '/bienvenida', 'Bienvenida', 
)
app = web.application(urls, globals())
render = web.template.render("views")

class Index:
    def GET(self): # se invoca al entrar a la ruta /login ENUMERAR
        try: # prueba el bloque de codigo
            message = None
            return render.bienvenida() # renderiza la pagina login.html 
        except Exception as error: # atrapa algun error
            message = "Error en el sistema"
            print("Error Bienvenida.GET: {}".format(error)) # se alamacena un mensaje de error ..... print("Error Login.POST: {}".format(error.args[0]))
            return render.bienvenida(message) 
    def GET(self): # se invoca al entrar a la ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Bienvenida.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return render.bienvenida()  # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                # Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.bienvenida() # renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Bienvenida.GET: {}".format(error))
            
    
if __name__ == "__main__":
    web.config.debug = False
    app.run()
    