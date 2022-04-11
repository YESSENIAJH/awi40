import pyrebase
import firebase_config as token
firebase = pyrebase.initialize_app(token.firebaseConfig)
db = firebase.database()

users = db.child("users").get()

for user in users:
    print(user.key(), user.val())

user = db.child("users").child("").get()

for user in users:
    print(u.key(), u.val())