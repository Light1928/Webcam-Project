import pyrebase

firebaseConfig = {
  'apiKey': "********************",
  'authDomain': "********************",
  'databaseURL': "********************",
  'projectId': "********************",
  'storageBucket': "********************",
  'messagingSenderId': "********************",
  'appId': "********************",
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
path_on_cloud = 'images/'
datadir = './images/'
all_files = storage.child("myfirebasefolder").list_files()

for file in all_files:
    try:
        file.download_to_filename(datadir + file.name)
    except:
        print('Download Failed')

