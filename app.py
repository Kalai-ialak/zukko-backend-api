from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)

# 1. Firebase Initialization (Direct setup)
# Unga folder-la irukura .json file name-ah inga correct-ah kudunga
try:
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Firebase connected successfully!")
except Exception as e:
    print(f"Error connecting to Firebase: {e}")

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Zukko API is running perfectly!",
        "database": "Firebase Connected",
        "author": "Kalai"
    })

# Port 6009-ah namma Docker-la map pannirukkom
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6009, debug=True)