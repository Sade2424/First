#import the required modules 
import firebase_admin
from firebase_admin import db, credentials 

#authenticate to firebase
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://tm-sade-default-rtdb.europe-west1.firebasedatabase.app/"})





#DON'T FORGET TO DO GIT COMMIT AT THE END (otherwise you're cooked) :)
