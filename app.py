from flask import Flask, jsonify
from firebase_config import df_firestore  # Firebase setup import panrom

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Zukko API is running perfectly!",
        "database": "Firebase Connected"
    })

# Intha part thaan romba mukkiyam! 
# host='0.0.0.0' kudutha thaan Docker veliya connect aagum.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)