import web
import pyrebase
import firebase_config as token
urls = (
    '/registrar', 'Registrar'
)
app = web.application(urls, globals())
render = web.template.render('views')


class Registrar:
    def GET(self):
        return render.registrar()

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
                
        return render.registrar()
    
if __name__ == "__main__":
    app.run()

