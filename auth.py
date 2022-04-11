import web
import pyrebase
import firebase_config as token
urls = (
    '/', 'Elegir'
)
app = web.application(urls, globals())
render = web.template.render('views')


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
                "email": email
            }
            results = db.child("users").child(user['localId']).set(data)
            return web.seeother("/")
            print(results)
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error'] 
            message = error['message']
            print("Error Login.POST: {}".format(message)) # se imprime el message enviado por firebase
            web.setcookie('localID', None, 3600)
    
if __name__ == "__main__":
    app.run()

