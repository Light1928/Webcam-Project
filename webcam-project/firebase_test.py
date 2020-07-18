import pyrebase
import firebase_admin
from firebase_admin import credentials
# firebaseConfig = {
#   'apiKey': "********************",
#   'authDomain': "********************",
#   'databaseURL': "********************",
#   'projectId': "********************",
#   'storageBucket': "********************",
#   'messagingSenderId': "********************",
#   'appId': "********************",
# }

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
datadir = './'
all_files = storage.child('images/').list_files()

for file in all_files:
    try:
        file.download_to_filename(datadir + file.name)
    except:
        print('Download Failed')

