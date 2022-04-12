import web
import pyrebase
import firebase_config as token
import json  #incluir libreria JSON uwu
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

urls = (
    '/', 'Login',
    '/bienvenida', 'Bienvenida', 
    '/recuperar', 'Recuperar',
    '/registrar', 'Registrar',
    '/logout','Logout',
    '/elegir','Elegir',
    '/admin','Admin',
    '/operador','Operador',
    '/sucursales','Sucursales',
    '/users_list','UsersList'
)
app = web.application(urls, globals())
render = web.template.render("views")

class Bienvenida:
    def GET(self): # se invoca al entrar a la ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Bienvenida.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return render.login()  # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                # Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.bienvenida() # renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Bienvenida.GET: {}".format(error)) # se imprime el error atrapado 


class Recuperar:
    def GET(self):
        return render.recuperar()

    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig) # se crea un objeto para conectarse con firebase
        auth = firebase.auth()
        formulario = web.input()
        email = formulario.email
        print(email)
        user = auth.send_password_reset_email(email)
        print(user)
        return render.recuperar() 

class Registrar:
    def GET(self): # se invoca al entrar a la ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("Registrar.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return web.seeother("login") # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                # Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.registrar() # renderiza login.html
        except Exception as error: # se atrapa algun error
            print("Error Registrar.GET: {}".format(error)) # se imprime el error

class Logout:
        def GET(self): 
            return render.login()  

class Sucursales:
    def GET(self): # se invoca al entrar a la ruta 
        try: # prueba el siguiente bloque de codigo
            print("Sucursales.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return render.login()  # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                # Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.sucursales() # renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Sucursales.GET: {}".format(error)) # se imprime el error atrapado 

class UsersList:
    def GET(self): # se invoca al entrar a la ruta /bienvenida
        try: # prueba el siguiente bloque de codigo
            print("UsersList.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return render.login()  # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                firebase = pyrebase.initialize_app(token.firebaseConfig) #coneccion con firebase
                db = firebase.database() #uso de base de datos
                users = db.child("users").get() #obtiene la informacion
                return render.users_list(users) # renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error UsersList.GET: {}".format(error)) # se imprime el error atrapado 

class Admin:
    def GET(self): # se invoca al entrar a la ruta 
        try: # prueba el siguiente bloque de codigo
            print("Admin.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return render.login()  # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                # Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.admin() # renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Admin.GET: {}".format(error)) # se imprime el error atrapado 

class Operador:
    def GET(self): # se invoca al entrar a la ruta 
        try: # prueba el siguiente bloque de codigo
            print("Operador.GET localID: ",web.cookies().get('localID')) # se imprime el valor de localID para verificarlos
            if web.cookies().get('localID') == None: # Si localID es None se redirecciona a login.html
                return render.login()  # se redirecciona al login.html
            else: # si la cookies no esta vacia 
                # Conectar con la base de datos de firebase para verificar que el usuario esta registrado, y obtener otros datos 
                return render.operador() # renderiza bienvenida.html
        except Exception as error: # se atrapa algun error
            print("Error Operador.GET: {}".format(error)) # se imprime el error atrapado


class Elegir:
    def GET(self):
        return render.elegir()

    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            db = firebase.database()
            formulario = web.input()
            auth = firebase.auth()
            db = firebase.database()
            name = formulario.name
            phone = formulario.phone
            email = formulario.email
            password = formulario.password
            tipo = formulario.tipo
            print(email,password)
            user = auth.create_user_with_email_and_password(email, password)
            local_id =(user['localId'])
            data ={
                "nombre": name,  
                "phone": phone, 
                "email": email,
                "tipo":tipo
            }
            results = db.child("users").child(user['localId']).set(data)
            return web.seeother("/admin")
            print(results)
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error'] 
            message = error['message']
            print("Error Login.POST: {}".format(message)) # se imprime el message enviado por firebase
            web.setcookie('localID', None, 3600)

class Login:
    def GET(self): # se invoca al entrar a la ruta /login
        try: # prueba el bloque de codigo
            message = None
            return render.login() # renderiza la pagina login.html 
        except Exception as error: # atrapa algun error
            message = "Error en el sistema"
            print("Error Login.GET: {}".format(error)) # se alamacena un mensaje de error ..... print("Error Login.POST: {}".format(error.args[0]))
            return render.login(message) 

    def POST(self): # se invoca al recibir el formulario
        try: # prueba el bloque de codigo 
            firebase = pyrebase.initialize_app(token.firebaseConfig) # se crea un objeto para conectarse con firebase
            auth = firebase.auth() # se crea un objeto para usar el servicios de autenticacion de firebase
            formulario = web.input() # Se crea una variable formulario para recibir los datos del login.html
            email = formulario.email # se almacena el valor de email del formulario
            password = formulario.password # se almacena el valor de password del formulario
            print(email,password) # se imprimen para verificar los valores recibidos
            user = auth.sign_in_with_email_and_password(email, password) #  autenticacion con firebase
            print(user["localId"]) # si los datos son correctos se recibe informacion del usuario imprime el localID
            web.setcookie('localID', user['localId'], 3600) # se almacena en una cookie el localID
            print("localId: ",web.cookies().get('localID')) # se imprime la cookie para verificar que se almaceno correctamente
            return web.seeother("bienvenida") # Redirecciona a otra pagina web 
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error'] 
            message = error['message']
            print("Error Login.POST: {}".format(message)) # se imprime el message enviado por firebase
            web.setcookie('localID', None, 3600)
            
    
if __name__ == "__main__":
    web.config.debug = False
    app.run()
    