import web

import pyrebase
import firebase_config as token
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

urls = (
    '/registrar', 'Registrar'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Registrar:
    def GET(self):
        return render.registrar()

    def POST(self):
        formulario = web.input()
        email = formulario.email
        password = formulario.password
        user = auth.create_user_with_email_and_password(email, password)
        print(user["localId"])
        return render.registrar()
    
if __name__ == "__main__":
    app.run()



    import web
import pyrebase
import firebase_config as token
import json
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

urls = (
    '/registrar', 'Registrar',
    '/login', 'Login',
)
app = web.application(urls, globals())
render = web.template.render('views')

class Login:
    def GET(self): # se invoca al entrar a la ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Login.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return web.seeother("registrar") # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                # Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.login() # renderiza login.html
        except Exception as error: # se atrapa algun error
            print("Error Login.GET: {}".format(error)) # se imprime el error

class Registrar:
    def GET(self):
        try:
            return render.registrar()
        except Exception as error:
            print("Error Registrar.POST: {}".format(error.args[0]))

    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            formulario = web.input()
            email = formulario.email
            password = formulario.password
            user = auth.create_user_with_email_and_password(email, password)
            print(user["localId"])
            print(email,password)
            return render.registrar()
            web.setcookie('localID', user['localId'], 3600) # se almacena en una cookie el localID
            print("localId: ",web.cookies().get('localID')) # se imprime la cookie para verificar que se almaceno correctamente
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error'] 
            message = error['message']
            print("Error Login.POST: {}".format(message))
            return render.registrar()

if __name__ == "__main__":
    app.run()
