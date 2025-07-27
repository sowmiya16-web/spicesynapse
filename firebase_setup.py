import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate("firebase-adminsdk.json")  # path to downloaded Firebase service account key
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-bucket-name.appspot.com'  # e.g., spicesynapse.appspot.com
})

db = firestore.client()
bucket = storage.bucket()
