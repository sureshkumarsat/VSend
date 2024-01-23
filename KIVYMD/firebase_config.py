import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDGvMHjKJwvIllrpnB7XrpJMSPyMXF5njk",
    "authDomain": "todo-notes-app-424d3.firebaseapp.com",
    "databaseURL": "https://todo-notes-app-424d3-default-rtdb.firebaseio.com",
    "projectId": "todo-notes-app-424d3",
    "storageBucket": "todo-notes-app-424d3.appspot.com",
    "messagingSenderId": "811101120479",
    "appId": "1:811101120479:web:921f65ce525f6a7cae466a",
    "measurementId": "G-LYBNEJ6WS4"
    }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
# tasks = db.child('varyirving2').child('Tasks').get()
# print(tasks.val())
# for task in tasks.each():
#     print(task.key())
#     print(task.val())
#     print(task.val()["date"])
#     print(task.val()["time"])
#     print(task.val()["frequency"])

# db.child('varyirving2').child('Tasks').child("task4").remove()