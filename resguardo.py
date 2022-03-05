import web

import pyrebase
import firebase_config as token
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

urls = (
    '/login', 'Login'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        formulario = web.input()
        email = formulario.email
        password = formulario.password
        user = auth.sign_in_with_email_and_password(email, password)
        print(user["localId"])
        return render.login()
    
if __name__ == "__main__":
    app.run()